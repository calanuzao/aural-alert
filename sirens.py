import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf
from IPython.display import Audio, display
import soundata

def initialize_dataset(data_home='/Users/calodii/Desktop/stuff/home/threed-audio/final/aural-alert'):
    """
    Initialize the dataset and load metadata
    """
    dataset = soundata.initialize('urbansound8k', data_home=data_home)
    metadata_path = os.path.join(dataset.data_home, 'metadata', 'UrbanSound8K.csv')
    metadata = pd.read_csv(metadata_path)

    return dataset, metadata

def sirens(file_ids, metadata_df=None, dataset=None):
    """
    Find and play specific siren files by their file IDs.
    
    Args:
        file_ids: List of file IDs to find
        metadata_df: Optional metadata DataFrame (will be loaded if not provided)
        dataset: Optional soundata dataset (will be initialized if not provided)
    
    Returns:
        List of dictionaries with siren data
    """
    # initialize dataset and metadata if not provided
    if metadata_df is None or dataset is None:
        dataset, metadata_df = initialize_dataset()
    
    # create output directory if needed
    output_dir = os.path.join(os.getcwd(), "experiment_sirens")
    os.makedirs(output_dir, exist_ok=True)
    
    # extract file information from metadata
    results = []
    
    for file_id in file_ids:
        # find the matching file in metadata
        file_info = metadata_df[metadata_df['slice_file_name'].str.startswith(file_id)]
        
        if len(file_info) == 0:
            print(f"❌ File {file_id} not found in metadata")
            continue
        
        file_info = file_info.iloc[0]
        
        # get file path
        audio_path = os.path.join(
            dataset.data_home,
            'audio',
            f'fold{file_info["fold"]}',
            file_info['slice_file_name']
        )
        
        # load and normalize audio
        audio, sr = librosa.load(audio_path, sr=48000)
        audio = audio / np.max(np.abs(audio))
        
        # save to experiment directory if needed
        output_path = os.path.join(output_dir, file_info['slice_file_name'])
        if not os.path.exists(output_path):
            sf.write(output_path, audio, 48000)
        
        # extract audio features
        duration = len(audio) / 48000
        rms = np.sqrt(np.mean(audio**2))
        peak = np.max(np.abs(audio))
        spec_centroid = librosa.feature.spectral_centroid(y=audio, sr=48000)[0].mean()
        
        # store result
        results.append({
            'filename': file_info['slice_file_name'],
            'fold': file_info['fold'],
            'class': file_info['class'],
            'fsID': file_info['fsID'],
            'start': file_info['start'],
            'end': file_info['end'],
            'duration': duration,
            'rms_level': rms,
            'peak_level': peak,
            'spectral_centroid': spec_centroid,
            'audio': audio,
            'sr': sr,
            'path': output_path
        })
    
    # display metadata table
    if results:
        results_df = pd.DataFrame([{k: v for k, v in r.items() if k not in ['audio', 'sr']} 
                                  for r in results])
        
        print(f"\nFound {len(results)} of {len(file_ids)} requested siren files:")
        display(results_df[['filename', 'fold', 'duration', 'rms_level', 'spectral_centroid']])
        
        # play each file with visualizations
        for r in results:
            print(f"\n{'-'*50}")
            print(f"File: {r['filename']}")
            print(f"Duration: {r['duration']:.2f} seconds")
            print(f"RMS Level: {r['rms_level']:.4f}")
            print(f"Spectral Centroid: {r['spectral_centroid']:.2f} Hz")
            print(f"Original Source ID: {r['fsID']}")
            print(f"Segment: {r['start']} to {r['end']} seconds")
            
            # plot waveform
            plt.figure(figsize=(10, 3))
            plt.plot(np.linspace(0, r['duration'], len(r['audio'])), r['audio'])
            plt.title(f"Waveform: {r['filename']}")
            plt.xlabel("Time (s)")
            plt.ylabel("Amplitude")
            plt.tight_layout()
            plt.show()
            
            # plot spectrogram
            plt.figure(figsize=(10, 4))
            D = librosa.amplitude_to_db(np.abs(librosa.stft(r['audio'])), ref=np.max)
            librosa.display.specshow(D, sr=r['sr'], x_axis='time', y_axis='log')
            plt.colorbar(format='%+2.0f dB')
            plt.title(f"Spectrogram: {r['filename']}")
            plt.tight_layout()
            plt.show()
            
            # play audio
            display(Audio(r['audio'], rate=r['sr']))
    
    else:
        print("No matching siren files found.")
    
    return results

# specific siren files to find and play
target_sirens = [
    '71177-8-1-1',
    '16772-8-0-0',
    '111671-8-0-5',
    '157868-8-0-7',
    '74364-8-1-5'
]

# only run this code if the file is executed directly (not imported)
if __name__ == "__main__":
    # Initialize dataset and metadata
    dataset, metadata = initialize_dataset()
    
    # Find and play these files
    siren_results = sirens(target_sirens, metadata, dataset)