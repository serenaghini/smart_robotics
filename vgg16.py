import torch
import torch.nn as nn
from torch import optim, nn
from torchvision import models, transforms
import numpy as np
import cv2
import sys
from numpy.linalg import norm

def vgg16(img1, img2):

 model = models.vgg16(pretrained=True)

 class FeatureExtractor(nn.Module):
   def __init__(self, model):
     super(FeatureExtractor, self).__init__()
     # Extract VGG-16 Feature Layers
     self.features = list(model.features)
     self.features = nn.Sequential(*self.features)
     # Extract VGG-16 Average Pooling Layer
     self.pooling = model.avgpool
     # Convert the image into one-dimensional vector
     self.flatten = nn.Flatten()
     # Extract the first part of fully-connected layer from VGG16
     self.fc = model.classifier[0]

   def forward(self, x):
     # It will take the input 'x' until it returns the feature vector called 'out'
     out = self.features(x)
     out = self.pooling(out)
     out = self.flatten(out)
     out = self.fc(out)
     return out

 # Initialize the model
 model = models.vgg16(pretrained=True)
 new_model = FeatureExtractor(model)

 # Change the device to GPU
 device = torch.device('cuda:0' if torch.cuda.is_available() else "cpu")
 new_model = new_model.to(device)

 # Transform the image, so it becomes readable with the model
 transform = transforms.Compose([
   transforms.ToPILImage(),
   transforms.CenterCrop(512),
   transforms.Resize(448),
   transforms.ToTensor()
 ])

 f1 = []
 img = cv2.imread(img1)
 img = img[155:305, 105:255]
 img = transform(img)
 img = img.reshape(1, 3, 448, 448)
 img = img.to(device)
 with torch.no_grad():
   feature = new_model(img)
 f1.append(feature.cpu().detach().numpy().reshape(-1))
 f1 = np.array(f1)

 f2 = []
 img = cv2.imread(img2)
 img = img[155:305, 105:255]
 img = transform(img)
 img = img.reshape(1, 3, 448, 448)
 img = img.to(device)
 with torch.no_grad():
   feature = new_model(img)
 f2.append(feature.cpu().detach().numpy().reshape(-1))
 f2 = np.array(f2)

 cosine = np.sum(f1*f2, axis=1)/(norm(f1, axis=1)*norm(f2, axis=1))

 print("Cosine Similarity:\n", cosine)

if __name__ == '__main__':
 img1 = sys.argv[1]
 img2 = sys.argv[2]
 vgg16(img1, img2)



