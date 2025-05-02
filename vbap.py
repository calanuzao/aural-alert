import numpy as np
import math
import csv
import os

"""
vpab implementation 
"""

# initializing custom speaker layout (azimuth, elevation in degrees) 
# following MTech's 6th Floor Audio Lab Booth
speakers = {
    "C":  (0, 0),
    "L":  (-30, 0),
    "R":  (30, 0),
    "Ls": (-90, 0),
    "Rs": (90, 0),
    "Lr": (-150, 0),
    "Rr": (150, 0),
    "Lt": (-90, 45),
    "Rt": (90, 45)
}

def spherical_to_cartesian(az_deg, el_deg):
    """
    Converts spherical coordinates (azimuth and elevation [in degrees]) into 
    3D Cartesian coordinates (x, y, z) by representing speaker positions as unit vectors
    in 3D space. The conversion takes the target sound direction into the same vector space
    and then the gains of each speaker is calculated through dot products between the target 
    direction speaker and the speaker vectors.

    Arguments:
        Azimuth (az): Horizontal angle in the x-y-plane (0 degrees is along +x axis)
        Elevation (el): Angle form the x-y-plane toward the z-axis
        Radius (r): Distance from origin (implicitly set to 1 in this function)

    Conversion Formulas:
    x = r * cos(el) * cos(az)
    y = r * cos(el) * sin(az)
    z = r * sin(el)

    Returns:
        3D Array Coordinates
    """
    az = math.radians(az_deg)
    el = math.radians(el_deg)
    x = math.cos(el) * math.cos(az)
    y = math.cos(el) * math.sin(az)
    z = math.sin(el)

    return np.array([x, y, z])

def calculate_vbap(az, el):
    """
    Calculates Vector Based Amplitude Panning (VBAP).

    Arguments:
        target: target direction as a vector
        vecs: unit vector
        raw: Dot product of target and speaker. Mwasures how closely each speaker is with the target direction.
        pos: Positve sound! No negative sound, it does not make sense.
        norm: Normalization that ensures sum of squares is 1 while mantaining consistent loudness.

    Returns:
        Normalized speaker gains.

    """
    # converting target direction to a unit vector
    target = spherical_to_cartesian(az, el)

    # converting all speaker positions to unit vectors
    vecs = {name: spherical_to_cartesian(a, e) for name, (a, e) in speakers.items()}

    # calculating the dot product between target and each speaker
    # higher values indicate better alignment
    raw = {n: np.dot(target, v) for n, v in vecs.items()}

    # zero out negative gains
    # only positive sound reproduction is possible
    pos = {n: max(0, g) for n, g in raw.items()}

    # normalize gains
    norm = np.linalg.norm(list(pos.values()))
    gains = {n: g/norm if norm>0 else 0 for n, g in pos.items()}

    return gains

def lin2db(x):
    """
    Converts a linear amplitude value to its equivalent in decibles (dB).

    Arguments:
        x: Linear amplitude value

    Returns:
        If x is positive, applies 30 * log10(x) --> dB = 20 * log10(amplitude ratio)
        Otherwise, it returns negative infinity
    """
    return 20 * math.log10(x) if x>0 else float('-inf')

if __name__ == "__main__":
    """
    Execution script.

    Arguments:
        Input sound source direction as:
            az = float(input("Azimuth (°): "))
            el = float(input("Elevation (°): "))
        
        Calculates VBAP:
            gains = calculate_vbap(az, el)

        Display results sorted by gain by showing speaker gains in both linear and dB formats. 
        Sorts speakers by gain (highest first) using the lambda function. 

    Returns:
        CSV filename incorporating the input angles.

    """
    az = float(input("Azimuth (°): "))
    el = float(input("Elevation (°): "))
    gains = calculate_vbap(az, el)
    print("\nSpeaker Gains (Linear & dB):")
    for spk, g in sorted(gains.items(), key=lambda i: -i[1]):
        print(f"{spk}: {g:.3f} ({lin2db(g):.1f} dB)")
    # csv export
    fname = f"VBAP_custom_az{int(az)}_el{int(el)}.csv"
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Speaker", "LinearGain", "Gain_dB"])
        for spk, g in gains.items():
            writer.writerow([spk, f"{g:.6f}", f"{lin2db(g):.2f}"])
    print(f"CSV saved as {fname}")