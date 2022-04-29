import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
import imageio
from PIL import Image
import math
import time

import numpy as np 

def padded_image(image, kernel): 

    """ This method takes a picture and a filter/kernel in the form of a matrix, 
        and based upon the size of the kernel, uses the logic of nearest neighbour 
        to pad the egdes og the picture."""

    image_height, image_width = image.shape
    pad_size_height = kernel.shape[0]//2
    pad_size_width = kernel.shape[1]//2
    # Adding pad_size to size of the original image
   
    padded_image = np.zeros((image_height+pad_size_height*2, image_width+pad_size_width*2))
    # Now that we have extended the picture on all sides, iteration will happen 
    # with respect to the new placing of the original image within the padded image frame 
    nh = image_height+pad_size_height
    nw = image_width+pad_size_width
    h = image_height
    w = image_width
    for i in range(0, nh+pad_size_height): 
        for j in range(0, nw+pad_size_width): 

            if i <= pad_size_height and j <= pad_size_width: 
                padded_image[i][j] = image[0][0]
                
            elif i <= pad_size_height and j >= nw: 
                padded_image[i][j] = image[0][w-1]

            elif j <= pad_size_width and i >= nh: 
                padded_image[i][j] = image[h-1][0]
            
            elif i >= nh and j >= nw: 
                padded_image[i][j] = image[h-1][w-1]
            
            elif i <= pad_size_height and pad_size_width < j < nw: 
                padded_image[i][j] = image[0][j-pad_size_width]
            
            elif i >= nh and pad_size_width < j < nw: 
                padded_image[i][j] = image[h-1][j-pad_size_width]
            
            elif pad_size_height < i < nh and j <= pad_size_width: 
                padded_image[i][j] = image[i-pad_size_height][0]
      
            elif pad_size_height < i < nh and j >= nw: 
                padded_image[i][j] = image[i-pad_size_height][w-1] 
            
            elif pad_size_height < i < nh and pad_size_width < j < nw:
                padded_image[i][j] = image[i-pad_size_height][j-pad_size_width]
    
    return padded_image, pad_size_height, pad_size_width

def convolve(image, kernel, ker_coef=1): 
    """
    This method takes as input a padded image, a kernel/filter and a kernel 
    coefficient and convolves the image by the kernel multiplied by kernel coefficient. 
    """
    for i in range(2): 
        kernel = np.rot90(kernel) 

    w = np.array(kernel[kernel.shape[0]//2, 0: kernel.shape[1]])
    v = np.array(kernel[:kernel.shape[0], kernel.shape[1]//2])

    if np.sum(abs(w)) == 0: 
        w = np.ones([kernel.shape[1]])
    elif np.sum(abs(v)) == 0: 
        v = np.ones([kernel.shape[0]])
   
    pad_image, k, h = padded_image(image, kernel)

    conv_image = np.zeros((image.shape))

    for i in range(k, image.shape[0]+k):
        for j in range(h, image.shape[1]+h):

            mat2 = pad_image[i-k:i+k+1, j-h:j+h+1]

            conv_image[i-k][j-h] = mat2@w@v.T*ker_coef

    return conv_image

def vec_convolve(image, kernel):
    return None

def generate_gauss_mask_sigma(sigma ,K=1):
    """
    Method for generating a gauss-kernel and it's coefficient. Pay notice to 
    the fact that the size of the kernel is directly connected to the scalar 
    value of sigma. 
    """
    
    side = math.ceil(1+8*sigma)
    y, x = np.mgrid[-side//2+1:(side//2)+1, -side//2+1:(side//2)+1]
    ker_coef = K/(2*np.pi*sigma**2)
    g = np.exp(-((x**2 + y**2)/(2.0*sigma**2)))

    return g, ker_coef

def generate_gauss_mask(side ,sigma ,K=1):
    
    y, x = np.mgrid[-side//2+1:(side//2)+1, -side//2+1:(side//2)+1]
    ker_coef = K/(2*np.pi*sigma**2)
    g = np.exp(-((x**2 + y**2)/(2.0*sigma**2)))

    return g, ker_coef

def gradients(image): 
    """
    This method calculates the gradients of the pixels in the picture 
    in both x and y direction, and then uses it to calculate the magnitude of 
    each pixel in the picture. 
    """
    
    grad_x_kernel = np.array([[-1, 0, 1], 
                              [-2, 0, 2],
                              [-1, 0, 1]])

    grad_y_kernel = np.array([[-1, -2, -1], 
                               [0, 0, 0],
                               [1, 2, 1]])

    grad_x_img = (convolve(image, grad_x_kernel))
 
    grad_y_img = (convolve(image, grad_y_kernel))
  

    grad_mag = (np.hypot(grad_x_img, grad_y_img))


    return grad_x_img, grad_y_img, (grad_mag/grad_mag.max())*255

def grad_dir(grad_x, grad_y):
    """
    Given the gradients in x and y direction, this method calculates the direction of the 
    gradients. 
    """

    angle = (np.round((np.arctan(grad_y/grad_x))*(180/np.pi)*1/45)*45)%180
    #angle = (np.degrees(np.arctan2(grad_y,grad_x)))
    #angle = np.where(angle >= 0, angle, 0)
    print(angle.shape)

    return angle

def define_dir(grad_angle, grads): 
    """
    This method moves through every single pixel in the image, and checks the direction of the gradient.
    It then sets it to one of four possible angles, and then thins the lines of the gradient. 
    """
    grad_angle_shape = grad_angle.shape
    width = grad_angle.shape[1]
    ex_width = width +1
    grad_angle = grad_angle.flatten()
    grads = grads.flatten()

    nonmaxima_image = np.zeros(grads.flatten().shape)

    for j in range(ex_width, len(nonmaxima_image)-width):

        if (-22.5 <= grad_angle[j] < 22.5): 
            if grads[j-1] <= grads[j] and grads[j+1] <= grads[j]: 
   
                nonmaxima_image[j] = int((grads[j]))
            else:
                nonmaxima_image[j] = 0
        elif (22.5 <= grad_angle[j] < 67.5):
            if grads[j-width-1] <= grads[j] and grads[j+width+1] <= grads[j]: 

                nonmaxima_image[j] = int((grads[j]))
            else:
                nonmaxima_image[j] = 0
        elif (67.5 <= grad_angle[j] < 112.5): 
            if grads[j-width] <= grads[j] and grads[j+width] <= grads[j]: 
     
                nonmaxima_image[j] = int((grads[j]))
            else:
                nonmaxima_image[j] = 0
        elif (112.5 <= grad_angle[j] < 157.5): 
            if grads[j-width+1] <= grads[j] and grads[j+width-1] <= grads[j]: 

                nonmaxima_image[j] = int((grads[j]))
            else:
                nonmaxima_image[j] = 0
        
    nonmaxima_image = nonmaxima_image.reshape(grad_angle_shape)
    return nonmaxima_image

def hysteresis(nonmaxima_image): 
    """
    This method checks the picture with now thinned lines and highlights each 
    pixel above the 'high' threshold, and then all pixels with values higher
    than, or equal to 'low' threshold. it then supresses all 'low' pixels 
    that aren't connected to strong pixels. 
    """

    non_shape = nonmaxima_image.shape
    width = nonmaxima_image.shape[1]
    ex_width = width +1
    nonmaxima_image = nonmaxima_image.flatten()
    out = np.zeros(nonmaxima_image.shape)

    high = 140
    low = 70

    strong = np.where(nonmaxima_image >= high)
    weak = np.where((low <= nonmaxima_image)  & (nonmaxima_image <= high))
    out[strong] = 255
    out[weak] = 75
    
    for j in range(ex_width, len(nonmaxima_image)-width): 

        if out[j] == 75: 
            if max(out[j-1], out[j+1],out[j-ex_width],out[j+ex_width],
                    out[j-width],out[j-width],out[j-width+1],out[j+width-1]):
                out[j] = 255
            else: 
                out[j] = 0 

    out = np.array(out).reshape(non_shape)

    return out

if __name__ == "__main__": 
    start = time.time()
    img = imageio.imread('cellekjerner.png', as_gray=True)
    img = np.array(img)

    ker, coef = generate_gauss_mask_sigma(7)

    con_image = convolve(img, ker, ker_coef=coef)

    grad_X, grad_Y, grads = gradients(con_image)

    angle = grad_dir(grad_X, grad_Y)

    non_max = define_dir(angle, grads)

    hyst = hysteresis(non_max)

    end = time.time()
    print(end - start)

    fig, ax = plt.subplots(2,3)

    imageio.imsave('oppgave2_bilde1.png', con_image)
    imageio.imsave('oppgave2_bilde2.png', grads)
    imageio.imsave('oppgave2_bilde3.png', non_max)
    imageio.imsave('oppgave2_bilde4.png', hyst)


    ax[0][0].imshow(img,cmap='gray',vmin=0,vmax=255,aspect='auto')
    ax[0][1].imshow(con_image,cmap='gray',vmin=0,vmax=255,aspect='auto')
    ax[0][2].imshow(grads,cmap='gray',vmin=0,vmax=255,aspect='auto')
    ax[1][0].imshow(non_max,cmap='gray',vmin=0,vmax=255,aspect='auto')
    ax[1][1].imshow(hyst,cmap='gray',vmin=0,vmax=255,aspect='auto')



    #imageio.imsave('edge.png', hyst)

    plt.show()



