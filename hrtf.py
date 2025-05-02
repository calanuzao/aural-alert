import numpy as np
import os
from scipy import signal
import sofar

def prepare_sadie_sofa(sofa_path):
    hrtf_sofa = sofar.read_sofa(sofa_path)
    hrir_data = np.array(hrtf_sofa.Data_IR)
    source_positions = np.array(hrtf_sofa.SourcePosition)
    
    hrtf_data = np.zeros((360, 180, 2, 256))
    
    for i in range(len(source_positions)):
        az = int(source_positions[i][0]) % 360
        # clamp elevation between 0 and 179
        el = min(179, max(0, int(source_positions[i][1] + 90)))
        
        for ear in range(2):
            hrir = hrir_data[i, ear].reshape(-1)
            hrir = signal.resample(hrir, 256)
            hrtf_data[az, el, ear] = hrir
    
    np.save('hrtf_database.npy', hrtf_data)
    return hrtf_data