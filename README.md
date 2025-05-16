# Aural Alert

**Aural Alert: Enhancing Emergency Alerts with VBAP Technology**  
**Authors:** Chris Lanuza & Ryan Carey  
**Date:** May 15, 2025

## Overview

Aural Alert is a research-driven project focused on improving the effectiveness and accessibility of emergency audio alerts using Vector Base Amplitude Panning (VBAP) technology. The project explores how spatialized 3D audio can increase urgency, clarity, and inclusivity-especially for individuals with hearing impairments.
 
## Motivation

Traditional emergency alarms (sirens, beeps) often lose their sense of urgency due to overexposure and lack of spatial information. This desensitization, combined with the challenges faced by hearing-impaired individuals, highlights the need for more advanced, accessible alert systems. Aural Alert investigates whether VBAP can help users-regardless of hearing ability-better localize and respond to emergency signals.

## What is VBAP?

Vector Base Amplitude Panning (VBAP) is a loudspeaker-based 3D audio technique that allows sounds to be positioned anywhere in space using arrays of speakers. By adjusting speaker gains, VBAP creates the illusion that an alarm originates from a specific direction, such as the location of a hazard or the nearest exit. This provides immediate directional cues without requiring headphones or wearable devices.

## Key Features

- **Spatialized Emergency Alerts:** Alarms can be rendered to come from the actual hazard location or guide users to safety.
- **Inclusive Design:** Improves accessibility for hearing-impaired users and benefits the general population.
- **No Wearables Needed:** Works through loudspeakers in public spaces, vehicles, or buildings.
- **Reduced Desensitization:** Embedding spatial cues helps maintain urgency and recognition.

## Limitations

- **Optimal Listening Area:** Best spatial accuracy is achieved near the center of the speaker array.
- **Coverage Challenges:** Large or irregular spaces may require more advanced or numerous speaker setups for uniform spatial effects.

## Repository

All documentation, code, protocols, and data are available at:  
https://github.com/calanuzao/aural-alert

---

**In summary:**  
Aural Alert leverages VBAP to make emergency signals more urgent, informative, and accessible, aiming to improve response times and safety for everyone, including those with hearing impairments.

---

# Experiment Notes

- The following notes are from a series of experiments conducted with a hearing-impaired user.
- Experiment user is hearing impaired, diagnosed with Sensory Neural Hearing Loss (SNHL H90.3) in both ears.
- Bilateral mid to high-frequency sensorineural hearing loss, either congenital or acquired; cause is still unknown.
- Hearing at low frequencies remains normal. Speech discrimination is 100% bilaterally.
- Tinnitus is present in both ears.
- Hearing aids were recommended for both ears. Hearing aids will help regardless of the cause.
- The user is not wearing hearing aids during the experiments.

---

## 71177-8-1-1

- **User Input:**
    - Azimuth: 291
    - Elevation: 4
- **Speaker Gains (Linear & dB):**
    - Ls: 0.612 (-4.3 dB)
    - Lt: 0.548 (-5.2 dB)
    - L: 0.509 (-5.9 dB)
    - C: 0.235 (-12.6 dB)
    - Lr: 0.103 (-19.8 dB)
    - R: 0.000 (-inf dB)
    - Rs: 0.000 (-inf dB)
    - Rr: 0.000 (-inf dB)
    - Rt: 0.000 (-inf dB)
- **Observations (PT):**
    - I perceived a sweeping sound that originated from directly behind me. The source moved in an arcing trajectory, rising upward and slightly to my left, eventually settling near the upper-left-center of my sound field. The motion was smooth and continuous, with subtle changes in volume and frequency that gave the impression of elevation and lateral movement through a 3D auditory space.
- **Reality:**
    - The source sound was two meters from the center speaker. All the user's observations were correct.

---

## 16772-8-0-0

- **User Inputs:**
    - Azimuth: 106
    - Elevation: 67
- **Speaker Gains (Linear & dB):**
    - Rt: 0.831 (-1.6 dB)
    - Lt: 0.349 (-9.1 dB)
    - Rs: 0.340 (-9.4 dB)
    - Rr: 0.255 (-11.9 dB)
    - R: 0.086 (-21.3 dB)
    - C: 0.000 (-inf dB)
    - L: 0.000 (-inf dB)
    - Ls: 0.000 (-inf dB)
    - Lr: 0.000 (-inf dB)
- **Observations (PT):**
    - Took a very long time to localize and said "up a bit to the right".
    - Localization was...
- **Reality:**
    - Two meters from the center speaker.

---

## 111671-8-0-5

- **User Inputs:**
    - Azimuth: 36
    - Elevation: 20
- **Speaker Gains (Linear & dB):**
    - R: 0.616 (-4.2 dB)
    - C: 0.501 (-6.0 dB)
    - Rt: 0.417 (-7.6 dB)
    - Rs: 0.364 (-8.8 dB)
    - L: 0.252 (-12.0 dB)
    - Ls: 0.000 (-inf dB)
    - Lr: 0.000 (-inf dB)
    - Rr: 0.000 (-inf dB)
    - Lt: 0.000 (-inf dB)
- **Observations (PT):**
    - Had to tilt head to "healthy ear" to properly localize sound to 35 azimuth.
    - Localization was correct.
- **Reality:**
    - 1.5 meters from the center speaker.

---

## 157868-8-0-7

- **User Inputs:**
    - Azimuth: 220
    - Elevation: 6
- **Speaker Gains (Linear & dB):**
    - Lr: 0.738 (-2.6 dB)
    - Ls: 0.482 (-6.3 dB)
    - Lt: 0.396 (-8.0 dB)
    - Rr: 0.256 (-11.8 dB)
    - C: 0.000 (-inf dB)
    - L: 0.000 (-inf dB)
    - R: 0.000 (-inf dB)
    - Rs: 0.000 (-inf dB)
    - Rt: 0.000 (-inf dB)
- **Observations (PT):**
    - Quite off, said straight to the left.
    - Localization was correct.
- **Reality:**
    - 1.5 meters from the center speaker.

---

## 74364-8-1-5

- **User Inputs:**
    - Azimuth: 145
    - Elevation: 0
- **Speaker Gains (Linear & dB):**
    - Rr: 0.772 (-2.2 dB)
    - Rs: 0.445 (-7.0 dB)
    - Lr: 0.328 (-9.7 dB)
    - Rt: 0.314 (-10.1 dB)
    - C: 0.000 (-inf dB)
    - L: 0.000 (-inf dB)
    - R: 0.000 (-inf dB)
    - Ls: 0.000 (-inf dB)
    - Lt: 0.000 (-inf dB)
- **Observations (PT):**
    - Two takes to successfully localize sound:
        - 1 up
        - 1 back
- **Reality:**
    - Right top was super quiet.
    - Sound source was mostly in the back.