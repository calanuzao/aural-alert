import numpy as np
from scipy import signal
from typing import Tuple, Optional
import pandas as pd
import librosa
import os

class SpatialProcessor:
    def __init__(self, sample_rate: int = 48000, dataset = None):
        """
        Initialize the spatial processor
        """
        self.sample_rate = sample_rate
        self.proximity_gain = 1.0
        self.dataset = dataset

    def load_audio(self, track_id: str) -> Tuple[np.ndarray, int]:
        """
        Load and normalize audio from the UrbanSound8K dataset.
        """
        metadata = pd.read_csv(os.path.join(self.dataset.data_home, 'metadata', 'UrbanSound8K.csv'))
        file_info = metadata[metadata['slice_file_name'].str.startswith(track_id)].iloc[0]
        
        audio_path = os.path.join(
            self.dataset.data_home,
            'audio',
            f'fold{file_info["fold"]}',
            file_info['slice_file_name']
        )
        
        # loading audio and resampling to 48kHz
        audio_data, sr = librosa.load(audio_path, sr=self.sample_rate)
        
        return audio_data, sr

    def process_emergency_signal(self, track_id: str,
                             urgency: float,
                             azimuth: float,
                             room_type: str = 'office') -> np.ndarray:
        """
        Process a single emergency signal with spatial audio effects.
        """
        audio, sr = self.load_audio(track_id)
        
        if sr != self.sample_rate:
            audio = signal.resample(audio, int(len(audio) * self.sample_rate / sr))
        
        hrtf = np.load('hrtf_database.npy')
        brir = np.load('brir_database.npy')
        
        spatialized = self.process_hrtf(audio, hrtf, azimuth, 0)
        urgent = self.apply_urgency(spatialized, urgency)
        final = self.apply_brir(urgent, brir, room_type)
        
        return final

    def process_hrtf(self, audio: np.ndarray, hrtf: np.ndarray,
                    azimuth: float, elevation: float) -> np.ndarray:
        """Apply HRTF processing to audio signal."""
        h_left, h_right = self._get_hrtf_filters(hrtf, azimuth, elevation)
        out_left = signal.fftconvolve(audio, h_left, mode='same')
        out_right = signal.fftconvolve(audio, h_right, mode='same')

        return np.vstack((out_left, out_right))

    def apply_urgency(self, audio: np.ndarray, urgency: float) -> np.ndarray:
        """
        Modify audio based on urgency level (0-1)
        """
        ild_boost = 1.0 + (urgency * 0.15)
        audio_fft = np.fft.rfft(audio, axis=1)
        freqs = np.fft.rfftfreq(audio.shape[1], 1/self.sample_rate)
        tilt = np.exp(urgency * freqs / self.sample_rate)
        audio_fft *= tilt

        return np.fft.irfft(audio_fft, axis=1)

    def apply_brir(self, audio: np.ndarray, brir: np.ndarray,
                  room_type: str = 'office') -> np.ndarray:
        """
        Apply room acoustics using BRIR.
        """
        rt60 = 0.3 if room_type == 'office' else 1.2
        decay = np.exp(-6.9 * np.arange(len(brir)) / (rt60 * self.sample_rate))
        brir_scaled = brir * decay[:, np.newaxis]

        return signal.fftconvolve(audio, brir_scaled, axes=1, mode='same')

    def _get_hrtf_filters(self, hrtf: np.ndarray,
                         azimuth: float, elevation: float) -> Tuple[np.ndarray, np.ndarray]:
        """
        Helper to get interpolated HRTF filters
        """
        idx_az = int((azimuth + 180) / 360 * hrtf.shape[0])
        idx_el = int((elevation + 90) / 180 * hrtf.shape[1])

        return hrtf[idx_az, idx_el, 0], hrtf[idx_az, idx_el, 1]