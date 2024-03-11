import numpy as np
import mne
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io


def load_eeg(set_file, tsv_file):
    """
    This function get as parameter the name of the .set file, and the
    metadata file. It returns the EEG data , the channel names and the
    sampling frequency.
    """
    # Load EEG data
    data =scipy.io.loadmat(set_file)
    # load the metadata
    metadata = pd.read_csv(tsv_file, sep='\t', header = 0)
    # get the channel names
    ch_names = metadata['name']
    # get the sampling frequency
    sfreq = metadata['sampling_frequency'][1]
    #get the electrode values from the eeg dictionary
    signals = data['data']
    # get the number of electrodes, number of samples and number of epochs
    Num_electrodes, Num_samples, Num_trials = signals.shape
    for i in range(Num_trials):
            if i== 0:
                eeg_data = signals[:,:,i].reshape(Num_electrodes, Num_samples)
            else:
                #horizontally stack the signals
                eeg_data = np.hstack((eeg_data, signals[:,:,i].reshape(Num_electrodes, Num_samples)))
                
   

    return eeg_data, ch_names, sfreq

# this is the file that has the annotations about sampling frequency, channels, etc.
tsv_file = 'openneuro/ds003775/derivatives/cleaned_epochs/sub-001/ses-t1/eeg/sub-001_ses-t1_task-resteyesc_desc-epochs_channels.tsv'
# this is the file that has the EEG data
data_file = 'openneuro/ds003775/derivatives/cleaned_epochs/sub-001/ses-t1/eeg/sub-001_ses-t1_task-resteyesc_desc-epochs_eeg.set'


#
data, ch_names, sfreq = load_eeg(set_file = data_file, tsv_file=tsv_file)
print(sfreq)
#print(ch_names)
print(type(data))