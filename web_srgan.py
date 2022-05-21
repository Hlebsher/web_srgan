import torch
import numpy as np
import matplotlib.pyplot as plt
import json
from PIL import Image
import cv2

from skimage.metrics import peak_signal_noise_ratio as PSNR
from skimage.metrics import structural_similarity as SSIM

from utils import convert_image, center_crop, convert_to_y_channel
from models import Generator

import streamlit as st
x = st.slider('x')
st.write(x, 'squared is', x * x)
