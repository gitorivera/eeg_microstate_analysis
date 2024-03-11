import numpy as np
import mne
import matplotlib.pyplot as plt
import pandas as pd

def load_eeg(file_name):
    # Load EEG data
    raw = mne.io.read_raw_brainvision(file_name, preload=True)
    # Filter data
    raw.filter(1, 40)
    # Get data
    data = raw.get_data()
    # Get channel names
    ch_names = raw.info['ch_names']
    # Get sampling frequency
    sfreq = raw.info['sfreq']
    return data, ch_names, sfreq

# this is the file that has the annotations about sampling frequency, channels, etc.
tsv_file = 'openneuro/ds003775/derivatives/cleaned_epochs/sub-001/ses-t1/eeg/sub-001_ses-t1_task-resteyesc_desc-epochs_channels.tsv'
# this is the file that has the EEG data
data_file = 'openneuro/ds003775/derivatives/cleaned_epochs/sub-001/ses-t1/eeg/sub-001_ses-t1_task-resteyesc_desc-epochs_eeg.set'
data, ch_names, sfreq = load_eeg(data_file)
print(ch_names)
