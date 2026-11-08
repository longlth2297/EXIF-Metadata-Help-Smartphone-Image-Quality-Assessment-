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


class CachedFeatureRegressor(nn.Module):
    """Matched resource-adapted head with optional bias-free metadata offset."""

    def __init__(self, metadata: bool, feature_dim: int = 2048, hidden_dim: int = 256) -> None:
        super().__init__()
        self.image_head = nn.Sequential(
            nn.LayerNorm(feature_dim),
            nn.Linear(feature_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_dim, 1),
        )
        self.metadata_head = nn.Linear(16, 1, bias=False) if metadata else None

    def forward(self, features, metadata=None):
        generic = self.image_head(features).squeeze(1)
        if self.metadata_head is None:
            return generic, generic
        if metadata is None:
            raise ValueError("Metadata model requires value and mask features")
        combined = generic + self.metadata_head(metadata).squeeze(1)
        return generic, combined
