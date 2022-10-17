from torch import nn
from torchvision import models

class FeatureExtractor(nn.Module):
  def __init__(self, model = models.vgg16(weights=True)):
    super(FeatureExtractor, self).__init__()
    self.features = list(model.features)
    self.features = nn.Sequential(*self.features)
    self.pooling = model.avgpool
    self.flatten = nn.Flatten()
    self.fc = model.classifier[0]
  
  def forward(self, x):
    out = self.features(x)
    out = self.pooling(out)
    out = self.flatten(out)
    out = self.fc(out) 
    return out