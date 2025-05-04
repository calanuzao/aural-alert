# Aural Alert
This project investigates how VBAP can improve the clarity, directionality, and urgency of emergency signals. By embedding spatial and contextual cues into alerts, we aim to enhance user response and decision-making in real-world scenarios, using both headphones and speakers.

#### Implementation Status
- ✅ Dataset loading and siren extraction
- ✅ Basic audio playback
- ✅ Spatial audio processing (Audio Lab)
- 🚧 Room acoustics simulation

# Experiment Notes
- The following notes are from a series of experiments conducted with a hearing impaired user.
- Experment user is hearing impaired conditioned to Sensory Neural Hearing Loss (SNHL H90.3) on both ears. 
- Bilateral mid to high-frequency sensorineural hearing loss, either congenitial or acquired, cause is still unknown.
- Hearing at low frequencies remains normal. Speech dscrimmination is 100% bilaterally.
- Tinnitus is present in both ears.
- Hearing aids were recommended for both ears. Hearing aids will help regardless of the cause.
- The user is not wearing hearing aids during the experimets.

## 71177-8-1-1 
- User Input:
    - Azimuth:291
    - Elevation:4
- Speaker Gains (Linear & dB):
    - Ls: 0.612 (-4.3 dB)
    - Lt: 0.548 (-5.2 dB)
    - L: 0.509 (-5.9 dB)
    - C: 0.235 (-12.6 dB)
    - Lr: 0.103 (-19.8 dB)
    - R: 0.000 (-inf dB)
    - Rs: 0.000 (-inf dB)
    - Rr: 0.000 (-inf dB)
    - Rt: 0.000 (-inf dB)
- Observations (PT)
    - I perceived a sweeping sound that originated from directly behind me. 
      The source moved in an arcing trajectory, rising upward and slightly to my left, 
      eventually settling near the upper-left-center of my sound field. The motion was smooth and continuous, 
      with subtle changes in volume and frequency that gave the impression of elevation and lateral movement 
      through a 3D auditory space.
- Reality
    - The source sound was two meters from the center speaker. All the user's obesrvations were correct.

## 16772-8-0-0 
- User Inputs:
    - Azimuth:106
    - Elevation:67
- Speaker Gains (Linear & dB):
    - Rt: 0.831 (-1.6 dB)
    - Lt: 0.349 (-9.1 dB)
    - Rs: 0.340 (-9.4 dB)
    - Rr: 0.255 (-11.9 dB)
    - R: 0.086 (-21.3 dB)
    - C: 0.000 (-inf dB)
    - L: 0.000 (-inf dB)
    - Ls: 0.000 (-inf dB)
    - Lr: 0.000 (-inf dB)
- Observations (PT)
    - Took a very long time to localize and said up a bit to the rigth
    - Localization was
- Reality
    - Two meters from the center speaker

## 111671-8-0-5 
- User Inputs:
    - Azimuth: 36
    - Elevation:20
- Speaker Gains (Linear & dB):
    - R: 0.616 (-4.2 dB)
    - C: 0.501 (-6.0 dB)
    - Rt: 0.417 (-7.6 dB)
    - Rs: 0.364 (-8.8 dB)
    - L: 0.252 (-12.0 dB)
    - Ls: 0.000 (-inf dB)
    - Lr: 0.000 (-inf dB)
    - Rr: 0.000 (-inf dB)
    - Lt: 0.000 (-inf dB)
- Observations (PT)
    - Had to tilt head to "healthy ear" to properly localize sound to 35 azimuth
    - Localization was correct
- Reality
    - 1.5 meters from the center speaker

## 157868-8-0-7 
- User Inputs
    - Azimuth: 220
    - Elevation: 6
- Speaker Gains (Linear & dB):
    - Lr: 0.738 (-2.6 dB)
    - Ls: 0.482 (-6.3 dB)
    - Lt: 0.396 (-8.0 dB)
    - Rr: 0.256 (-11.8 dB)
    - C: 0.000 (-inf dB)
    - L: 0.000 (-inf dB)
    - R: 0.000 (-inf dB)
    - Rs: 0.000 (-inf dB)
    - Rt: 0.000 (- inf dB)
- Observations (PT)
    - Quite off, said straight to the left
    - Localization was correct
- Reality
    - 1.5 meters from the center speaker

## 74364-8-1-5 
- User Inputs:
    - Azimuth:145
    - Elevation: 0
- Speaker Gains (Linear & dB):
    - Rr: 0.772 (-2.2 dB)
    - Rs: 0.445 (-7.0 dB)
    - Lr: 0.328 (-9.7 dB)
    - Rt: 0.314 (-10.1 dB)
    - C: 0.000 (-inf dB)
    - L: 0.000 (-inf dB)
    - R: 0.000 (-inf dB)
    - Ls: 0.000 (-inf dB)
    - Lt: 0.000 (-inf dB)
- Observations (PT)
    - Two takes to succesfully localize sound
        - 1 up
        - 1 back
- Reality
    - Right top was super quite/
    - Sound source was mostly in the back.
