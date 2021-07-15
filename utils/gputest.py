import logging
import os

import torch


	
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
logging.getLogger().setLevel(logging.INFO)
logging.info(f'Using device {device}')
