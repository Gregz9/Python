import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
import imageio
from PIL import Image
import math

image = imageio.imread('portrett.png', as_gray=True)
image2 = imageio.imread('mask.png', as_gray=True)

def lin_trans(image, new_mean, new_std): 

    height, width = image.shape

    a = round(new_std/image.std(), 2) 
    
    b = new_mean - a*image.mean()
    

    f_out = np.zeros((height,width))
    for i in range(1, height): 
        for j in range(1, width): 
            f_out[i][j] = image[i][j]*a + b
            if(f_out[i][j] < 0): 
                f_out[i][j] = 0 
    print(f_out.mean())
    return f_out 


def find_points(old_points, new_points):
    
    matrix = np.array([[old_points[0][0], old_points[0][1], 1],
                       [old_points[1][0], old_points[1][1], 1],
                       [old_points[2][0], old_points[2][1], 1]])
    
    x_vec = np.array([new_points[0][0], new_points[1][0], new_points[2][0]])
    y_vec = np.array([new_points[0][1], new_points[1][1], new_points[2][1]])    

    a_coef = np.linalg.solve(matrix, x_vec)
    b_coef = np.linalg.solve(matrix, y_vec)
    
    affine_mat = np.array([[a_coef[0], a_coef[1], a_coef[2]], 
                           [b_coef[0], b_coef[1], b_coef[2]], 
                           [    0,          0,        1   ]])
    
    return affine_mat

def forward(image, matrix): 

    height, width  = image.shape
    print(height, width)
    new_height = 600
    new_width = 512
    new_image = np.zeros((new_height, new_width))

    
    for h in range(width):
        for w in range(height): 
            x = h 
            y = w

            xy_vector = np.array([[x],
                                [y], 
                                [1]]) 
           
            t3 =matrix@xy_vector
          
            new_x = round(t3[0][0])
            new_y = round(t3[1][0])
     
            #print(new_x, new_y)

            if(new_x in range(new_width)) and (new_y in range(new_height)):
                new_image[new_y][new_x] = image[y][x]
                      
    return new_image

def inverse_map(image, matrix):

    width, height = image.shape
    new_height = 600
    new_width = 512 
    matrix = np.linalg.inv(matrix)
    new_image = np.zeros((new_height, new_width))

    for w in range(new_width): 
        for h in range(new_height): 

            xy_vector = np.array([[w], [h], [1]])

            inv_trans = matrix@xy_vector

            new_x = round(inv_trans[0][0])
            new_y = round(inv_trans[1][0])

            if not (0 <= new_x < 600) or not(0<= new_y < 512):
                continue
            
            new_image[h,w] = image[new_y][new_x]
            
    return new_image

def binverse_map(image, matrix): # original

    new_height = 600
    new_width = 512 
    matrix = np.linalg.inv(matrix)
    new_image = np.zeros((new_height, new_width))

    for x in range(new_width): 
        for y in range(new_height): 

            xy_vector = np.array([[x], [y], [1]])

            inv_trans = matrix@xy_vector
            new_x = (inv_trans[0][0])
            new_y = (inv_trans[1][0])

            x0 = math.floor(new_x)
            y0 = math.floor(new_y)
            x1 = math.ceil(new_x)
            y1 = math.ceil(new_y)

            if not (0 <= new_x < 600) or not(0<= new_y < 512):
                continue
            
            if (x0 == x1 or y0 == y1): 
                new_image[y][x] = image[y0][x0]
                continue

            A = np.array([[ y0, x0, x0*y0, 1],
                          [ y0, x1, y0*x1, 1],
                          [ y1, x0, y1*x0, 1],
                          [ y1, x1, x1*y1, 1]])


            b = np.array([
                            image[y0][x0],
                            image[y0][x1],
                            image[y1][x0],
                            image[y1][x1]
                            ])

            s = np.linalg.solve(A,b)
            #print(s)
            new_image[y][x] = s[0]*new_y + s[1]*new_x + s[2]*new_x*new_y + s[3]
            
    return new_image

old_points = [[84,88], [119,68],[128,108]]
new_points = [[169, 257], [341, 257], [255, 439]]
mat = find_points(old_points, new_points)

linear_im = lin_trans(image, 127, 64)
new_image3 = forward(linear_im, mat)

new_image = inverse_map(image,mat)
new_image = lin_trans(new_image, 127, 64)
new_image2 = binverse_map(image, mat)
new_image2 = lin_trans(new_image2, 127, 64)

imageio.imsave('oppgave1_bilde4.png', linear_im)
imageio.imsave('oppgave1_bilde1.png', new_image3)
imageio.imsave('oppgave1_bilde2.png', new_image)
imageio.imsave('oppgave1_bilde3.png', new_image2)

fig, ax = plt.subplots(1, 3)

ax[0].imshow(new_image3,cmap='gray',vmin=0,vmax=255,aspect='auto')
ax[1].imshow(new_image,cmap='gray',vmin=0,vmax=255,aspect='auto')
ax[2].imshow(new_image2,cmap='gray',vmin=0,vmax=255,aspect='auto')

plt.show()
