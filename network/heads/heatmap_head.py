import torch
import torch.nn as nn

from torchinfo import summary


class SMP_HeatMapHead(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        layers = []

        layers.append(
            nn.Conv2d(
                in_channels=int(cfg["smp"]["decoder_output_classes"]),
                out_channels=32,
                kernel_size=3,
                padding=1

            ))
        layers.append(nn.ReLU(inplace=True))
        layers.append(nn.BatchNorm2d(32))
        layers.append(
            nn.Conv2d(
                in_channels=32,
                out_channels=256,
                kernel_size=3,
                padding=1,

            ))
        layers.append(nn.ReLU(inplace=True))
        layers.append(nn.BatchNorm2d(256))
        layers.append(
            nn.Conv2d(
                in_channels=256,
                out_channels=1,
                kernel_size=3,
                padding=1,

            ))
        layers.append(nn.ReLU(inplace=True))
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return self.model.forward(x)

    def print_details(self):
        batch_size = 32
        summary(self.model, input_size=(batch_size, 256, 96, 96))
