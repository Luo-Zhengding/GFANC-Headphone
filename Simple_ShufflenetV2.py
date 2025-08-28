import torch
import torchvision.models as models
import torch.nn as nn


class Modified_ShufflenetV2(nn.Module):
    def __init__(self, num_classes=6):
        super().__init__()

        self.bw2col = nn.Sequential(
            nn.BatchNorm2d(1),
            nn.Conv2d(1, 10, 1, padding=0), nn.ReLU(),
            nn.Conv2d(10, 3, 1, padding=0), nn.ReLU())

        self.mv2_base_fre = models.shufflenet_v2_x0_5(weights='DEFAULT') # pre-trained on ImageNet
        self.avg_pool_fre = nn.AdaptiveAvgPool2d((1, 1))

        self.freq_fc = nn.Sequential(
            nn.Linear(96, num_classes),
            nn.Sigmoid()) # !!! add Sigmoid

    def forward(self, x): # torch.Size([1, 1, 64, 26])
        x = self.bw2col(x) # torch.Size([1, 3, 64, 26])
        x = self.mv2_base_fre.conv1(x) # torch.Size([1, 24, 32, 13])
        x = self.mv2_base_fre.maxpool(x) # torch.Size([1, 24, 16, 7])
        x = self.mv2_base_fre.stage2(x) # torch.Size([1, 48, 8, 4])
        x = self.mv2_base_fre.stage3(x) # torch.Size([1, 96, 4, 2])
        x = self.avg_pool_fre(x).squeeze(-1).squeeze(-1) # torch.Size([1, 96])
        out = self.freq_fc(x)
        return out