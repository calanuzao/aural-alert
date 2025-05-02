import numpy as np
from scipy import signal

def create_brir_database():
    """Create synthetic BRIRs for different room types"""
    # Fixed parameters
    sr = 48000
    duration = 1.0  # Fixed 1 second duration for both room types
    n_samples = int(duration * sr)
    
    def create_room_ir(rt60):
        time = np.linspace(0, duration, n_samples)
        decay = np.exp(-6.9 * time / rt60)
        ir = np.random.randn(n_samples) * decay
        return ir / np.max(np.abs(ir))
    
    # Create room responses with same length
    office_brir = create_room_ir(0.3)   # 300ms RT60 for office
    hallway_brir = create_room_ir(1.2)  # 1.2s RT60 for hallway
    
    # Stack into 2D array (2 rooms x samples)
    brir_data = np.stack([office_brir, hallway_brir])
    
    # Save database
    np.save('brir_database.npy', brir_data)
    return brir_data

if __name__ == '__main__':
    create_brir_database()