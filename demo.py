#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:38:23 2018

@author: asem
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


image1 = mpimg.imread("images.jpg")
image2 = mpimg.imread("cameraman1.png")

image2 = np.array( image2 , dtype = np.float32 )


print( image1.shape )
print( image2.shape )

plt.figure()
plt.imshow(image1)

plt.figure()
plt.gray()
plt.imshow(image2)

plt.figure()
plt.hist( image2.flatten() , 128 )

plt.show()