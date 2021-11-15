import numpy as np
import torchvision
import random

dataset = torchvision.datasets.CIFAR10(root='./data', train=False, download=False)
images = []
soft_labels = []
for image, label in dataset:
    image = np.array(image)
    images.append(image)
    soft_label = np.zeros(10)
    soft_label[label] += random.uniform(0, 10) # an unnormalized soft label vector
    soft_labels.append(soft_label)
images = np.array(images)
soft_labels = np.array(soft_labels)
print(images.shape, images.dtype, soft_labels.shape, soft_labels.dtype)
np.save('data.npy', images)
np.save('label.npy', soft_labels)