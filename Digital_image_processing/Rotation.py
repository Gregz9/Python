from pickle import TRUE
import numpy as np 
from PIL import Image 
import matplotlib 
import matplotlib.pyplot as plt 
import imageio
from numba import jit 
import scipy.misc as sm
def change_angle_to_radian(angle): 
    angle_radius = angle * (np.pi/100)

def rotate(image, matrix): 

    height, width  = image.shape

    new_image = np.zeros((image.shape))


    for h in range(height):
        for w in range(width): 
            x = h 
            y = w
            #print(x, y)

            xy_vector = np.array([[x],
                                [y], 
                                [1]]) 
           
            t3 =matrix@xy_vector
          
            new_x = int(t3[0][0])
            new_y = int(t3[1][0])

            t1 = np.array([[new_x], 
                          [new_y], 
                           [1]])
            t4 = matrix2.dot(t1)  

            old_x = int(t4[0][0])
            old_y = int(t4[1][0])

            if(new_x in range(height)) and (new_y  in range(width)):
                new_image[x,y] = image[new_x][new_y]

            #if(new_x in range(height)) and (new_y  in range(width)):
             #   new_image[new_x,new_y] = image[x][y]
               
                    
    return new_image

def shear(image, matrix): 
    height, width  = image.shape

    new_image = np.zeros((int(height*3.5294), int(width*1.7594)))


    for h in range(height):
        for w in range(width): 
            x = h 
            y = w

            xy_vector = np.array([[x],
                                [y], 
                                [1]]) 
           
            t3 =matrix@xy_vector
          
            new_x = int(t3[0][0])
            new_y = int(t3[1][0])

            if(new_x in range(int(height*3.5294))) and (new_y in range(int(width*1.7594))):
                new_image[new_x,new_y] = image[x][y]
    return new_image

image_loaded = imageio.imread('portrett.png', as_gray=True)
angle = np.pi/4.5
height, width = image_loaded.shape 
coordinates = [int(height//2), int(width//2)]
    
rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0], 
                            [np.sin(angle), np.cos(angle), 0],
                            [0  ,   0   ,  1  ]])

translation_matrix1 = np.array([[1, 0, coordinates[0]],
                                [0, 1, coordinates[1]],
                                [0, 0, 1]])

translation_matrix2 = np.array([[1, 0, -1*coordinates[0]],
                                [0, 1, -1*coordinates[1]],
                                [0, 0, 1]])

hor = np.array([[1, 0.17, -50],
                [0.15, 1, -25],
                [0, 0, 1]])

hor2 = np.array([[3.5294, 0, 0],
                [0, 1.7594, 0],
                [0, 0, 1]])

sh1 =  np.array([[1, 0.5, 0],
                [0, 1, 0],
                [0, 0, 1]])

matrix = translation_matrix1@rotation_matrix@translation_matrix2@hor

matrix2 = np.linalg.inv(matrix)
new_image = rotate(image_loaded, matrix)
image2 = shear(image_loaded, hor2)
new_image2 = rotate(image2, matrix)

im2 = matplotlib.image.imsave('new_image.png', new_image, cmap='gray')
im2 = matplotlib.image.imsave('new_image2.png', image2, cmap='gray')
im2 = matplotlib.image.imsave('new_image3.png', new_image2, cmap='gray')

fig, ax = plt.subplots(1, 2)
ax[0].imshow(new_image,cmap='gray',vmin=0,vmax=255,aspect='auto')
ax[1].imshow(image_loaded,cmap='gray',vmin=0,vmax=255,aspect='auto')

plt.show()