import os

import torch

device = torch.device('cpu')  # sets device for model and PyTorch tensors

# Model parameters
image_w = 112
image_h = 112
channel = 3
emb_size = 128

# Training parameters
num_workers = 4  # for data-loading; right now, only 1 works with h5py
grad_clip = 5.  # clip gradients at an absolute value of
print_freq = 100  # print training/validation stats  every __ batches
checkpoint = None  # path to checkpoint, None if none

# Data parameters
num_classes = 85742
num_samples = 5822653
DATA_DIR = 'data'
faces_ms1m_folder = 'data/faces_emore'
path_imgidx = os.path.join(faces_ms1m_folder, 'train.idx')
path_imgrec = os.path.join(faces_ms1m_folder, 'train.rec')
IMG_DIR = 'data/images'
pickle_file = 'data/faces_ms1m_112x112.pickle'
