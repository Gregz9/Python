import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
import imageio
from PIL import Image

image = imageio.imread('portrett.png', as_gray=True)

#img_array = np.array(image)


height, width = image.shape

#print(image.std())
#print(image.mean())

a = round(64/image.std(), 2) 
print(a)
print(a*image.mean())
b = int(127 - a*image.mean())
print(b)

f_out = np.zeros((height,width))
for i in range(1, height): 
    for j in range(1, width): 
        f_out[i][j] = image[i][j]*a + b
        if(f_out[i][j] < 0): 
            f_out[i][j] = 0 


print('the new mean of the processed pricture: ', f_out.mean())

#trans_image = imageio.imsave('outfile.png', image)

plt.figure()
plt.imshow(f_out,cmap='gray',vmin=0,vmax=255,aspect='auto')
plt.title('f_out')
plt.show()
