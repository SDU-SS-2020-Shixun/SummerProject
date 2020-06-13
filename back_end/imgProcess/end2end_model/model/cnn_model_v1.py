import sys
sys.path.append('../')

import torch.nn as nn
from end2end_model.training_set_gen import gen_config

# CNN Model (2 conv layer)
class CNN_v1(nn.Module):
    def __init__(self):
        super(CNN_v1, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32,affine=True),
            # nn.Dropout(0.5),  # drop 50% of the neuron
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64,affine=True),
            # nn.Dropout(0.5),  # drop 50% of the neuron
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.layer3 = nn.Sequential(
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64,affine=True),
            # nn.Dropout(0.5),  # drop 50% of the neuron
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.fc = nn.Sequential(
            nn.Linear((gen_config.IMAGE_WIDTH//8)*(gen_config.IMAGE_HEIGHT//8)*64, 1024),
            nn.Dropout(0.5),  # drop 50% of the neuron
            nn.BatchNorm1d(1024, affine=True),
            nn.ReLU())
        self.rfc = nn.Sequential(
            nn.Linear(1024, gen_config.MAX_CAPTCHA*gen_config.ALL_CHAR_SET_LEN),
            nn.Dropout(),
            nn.BatchNorm1d(gen_config.MAX_CAPTCHA*gen_config.ALL_CHAR_SET_LEN,affine=True)
        )

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        out = out.view(out.size(0), -1)
        out = self.fc(out)
        out = self.rfc(out)
        return out