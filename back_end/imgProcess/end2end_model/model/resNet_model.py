import sys
sys.path.append('../')

import torch.nn as nn
import torchvision as tv
from end2end_model.training_set_gen import gen_config

# CNN Model (2 conv layer)
class ResNet34(nn.Module):
    def __init__(self):
        super(ResNet34, self).__init__()
        self.conv1=nn.Conv2d(1,3,3,1,1)
        self.model=tv.models.resnet18(pretrained=False)
        for param in self.model.parameters():
            param.requires_grad=True
        num_fc_ftr = self.model.fc.in_features
        self.model.fc=nn.Linear(num_fc_ftr,gen_config.MAX_CAPTCHA*gen_config.ALL_CHAR_SET_LEN)

    def forward(self, x):
        x=self.conv1(x)
        out = self.model(x)
        return out