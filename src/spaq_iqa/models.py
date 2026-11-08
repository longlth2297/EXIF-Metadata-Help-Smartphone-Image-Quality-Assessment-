"""Paper-aligned image-only model constructors."""

from __future__ import annotations

from torch import nn
from torchvision.models import ResNet50_Weights, resnet50


def build_resnet50_regressor(pretrained: bool = True) -> nn.Module:
    """ResNet-50 with scalar head, matching SPAQ BL's stated architecture."""
    weights = ResNet50_Weights.IMAGENET1K_V2 if pretrained else None
    model = resnet50(weights=weights)
    model.fc = nn.Linear(model.fc.in_features, 1)
    return model
