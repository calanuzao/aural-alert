# spatial audio stack
# hrtf/vbap/brir processing chain

import numpy as np
from scipy import signal
from typing import Tuple, Optional

class SpatialProcessor:
    def __init__(self, sample_rate: int = 48000):
        self.sample_rate = sample_rate
        self.proximity_gain = 1.0

    def process_hrtf(self, audio: np.ndarray, hrtf: np.ndarray,
                     azimuth: float, elevation: float) -> np.ndarray:
        """
        Apply HRTF processing to audio signal.
        """
        # get interpolated HRTF for given direction
        h_left, h_right = self._get_hrtf_filters(hrtf, azimuth, elevation)

        # apply HRTF convolution
        out_left = signal.fftconvolve(audio, h_left, mode='same')
        out_right = signal.fftconvolve(audio, h_right, mode='same')

        return np.vstack((out_left, out_right))
    
    def apply_urgency(self, audio: np.ndarray, urgency: float) -> np.ndarray:
        """
        Modify audio based on urgency level (0-1)
        """
        # increase ILD for higher urgency
        ild_boost = 1.0 + (urgency * 0.15)

        # apply spectral tilt for urgency
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
        # simplified HRTF interpolation
        idx_az = int((azimuth + 180) / 360 * hrtf.shape[0])
        idx_el = int((elevation + 90) / 180 * hrtf.shape[1])
        return hrtf[idx_az, idx_el, 0], hrtf[idx_az, idx_el, 1]