from tkinter.messagebox import QUESTION
import numpy as np 
import matplotlib.pyplot as plt 
import imageio 
import math 
import time 
from numpy.fft import fft2 
from scipy import signal
import cv2 
import matplotlib as mb
import sys
from numba import jit
import skimage.measure



# The coded is transformed into C-code by the use of numba, as it takes less time running it in C than python

# FUNTIONS/METHODS FOR USE IN TASK II

@jit
def DCT8x8(image, Q):      
                                                                                                 
    image = image - 128 # subtracting 128 from each pixel in the picture, thus lowering the intensity in the picture                         
    image_DCT = np.zeros((image.shape))                                                                                               
    for i in range(0, image.shape[0], 8):                                                                                             
        for j in range(0, image.shape[1], 8):                                                                                         
                                                                                                                                      
            block_F = np.zeros((8,8)) # block for inserting new values                                                                
            block_x = image[i:i+8, j:j+8].copy()                                                                                      
                                                                                                                                      
            for u in range(8):                                                                                                     
                for v in range(8):                                                                                                 
                    # values of the variables c_u and c_v are dependent on the indexes u and v                                                                                            
                    c_u=(1/np.sqrt(2)) if u == 0 else 1                                                                             
                    c_v=(1/np.sqrt(2)) if v == 0 else 1                                                                             
                                                                                                                                  
                    for x in range(8):                                                                                              
                        for y in range(8):                                                                                         
                                                                                                                                      
                            block_F[u,v] += np.cos((((2*x)+1)*u*np.pi)/16)*np.cos((((2*y)+1)*v*np.pi)/16)*block_x[x,y]                        
                                                                                                                                                                                                                                                                                                     
                    block_F[u,v] = round(((1/4)*c_u*c_v*block_F[u,v])/Q[u,v]) # Compression performed by element-wise division by the q*Q                  
                                                                                                                                      
            image_DCT[i:i+8, j:j+8] = block_F                                                                                         
    return image_DCT                                                                                                                  

@jit                                                                                                                                   
def iDCT8x8(image, Q):    
                                                                                                            
    f_out = np.zeros((image.shape))                                                                                                   
                                                                                                                                      
    for i in range(0, image.shape[0], 8):                                                                                             
        for j in range(0, image.shape[1], 8):                                                                                         
                                                                                                                                    
            block = np.zeros((8,8))                                                                                                   
            block2 = image[i:i+8, j:j+8].copy()                                                                                       
                                                                                                                                      
            for x in range(8):                                                                                                     
                for y in range(8):                                                                                                 
                                                                                                                                      
                    for u in range(8):                                                                                              
                        for v in range(8):                                                                                         
                            cu=(1/np.sqrt(2)) if u == 0 else 1                                                                        
                            cv=(1/np.sqrt(2)) if v == 0 else 1                                                                   

                            # In the DCT transform we element-wise divided by the 8x8 block by the elements of the product q*Q
                            # In the inverse DCT-transform, we have to element-wise mulitply the elements of the 8x8 block 
                            # in order to restorethe picture correclty     
                            block[x,y] += np.cos((((2*x)+1)*u*np.pi)/16)*np.cos((((2*y)+1)*v*np.pi)/16)*cu*cv*block2[u,v]*Q[u,v]    
                    block[x,y] = round((1/4)*block[x,y])
            
                                                                                                                
            f_out[i:i+8, j:j+8] = block                                                                                              
    return (f_out +128)                                                                                                               

    # Comment on the output of the method                                                                                             
    # After performing the division of 8x8-blocks contating the new values in cosiuns domain,                                         
    # and then rounding them to the closest int-values, it turned out that rounding the output                                        
    # of IDCT was corrupted. Henceforth I do not around the pixel-values in the reconstructed picture,                                
    # but the values returned are integers.                                                                                           

@jit                                                                                                                                 
def calculate_enthropy(image):  
    
    hist = dict()
                                                                                                          
    for i in range(image.shape[0]):                                                                                                   
        for j in range(image.shape[1]): 
            if int(image[i,j]) not in hist:         
                hist[int(image[i,j])] = 1
            else:                                                                                     
                hist[int(image[i,j])] += 1  
    #print(hist)
    ent = 0
    count = 0
    for intensity in hist: 
        pi = hist[intensity]/image.size
        if pi < 0: 
            count+=1 
        ent += pi*np.log2(pi)
    print(count)
    return (-ent)        
                                                                                                                                                                                                                                                                                                        
@jit                                                                                                                                  
def calculate_comp_rate(org_image_ent, new_image_ent, image):                                                                         
    # Returns an compression rate and an estimate of the memory used by the compressed image                                                                                                                                  
    cR = org_image_ent/new_image_ent                                                                                                    
    return cR             

@jit
def calculate_memory(image_ent, image): 
        mem = (image.shape[0]*image.shape[1]*image_ent)/(8*(10**3))
        return mem
                                                                                                                                    
# MAIN-RUN SECTION OF THE CODE                                                                                                        
                                                                                                                                      
if __name__ == '__main__':                                                                                                            
    big_q = np.array([[16, 11, 10, 16, 24, 40, 51, 61],                                                                               
                    [12, 12, 14, 19, 26, 58, 60, 55],                                                                                 
                    [14, 13, 16, 24, 40, 57, 69, 56],                                                                                 
                    [14, 17, 22, 29, 51, 87, 80, 62],                                                                                 
                    [18, 22, 37, 56, 68, 109, 103, 77],                                                                               
                    [24, 25, 55, 64, 81, 104, 113, 92],                                                                               
                    [49, 64, 78, 87, 103, 121, 120, 101],                                                                             
                    [72, 92, 95, 98, 112, 100, 103, 99]])                                                                             
                                                                                                                                      
    image_to_open = imageio.imread(sys.argv[1], as_gray=True)                                                                         
    org_ent = calculate_enthropy(image_to_open)   
                                                                         
    q = float(sys.argv[2])                                                                                                            
    # Those two lines of code are commented out, since I perform compression using a values og q from                                 
    # the array below: q_values.                                                                                                      
    #image = DCT8x8(image_to_open, big_q, q)                                                                                                                                                                                                                            
    #image2 = iDCT8x8(image)                                                                                                          
                                                                                                                                      
    q_values = [0.1, 0.5, 2, 8, 32]                                                                                                   
    compressed_pictures = []                                                                                                          
    ent_vals = []                                                                                                                    
                                                                                                                                    
    for i in range(len(q_values)): 
        Q = big_q*q_values[i]   
        #print(Q)                                                                                                
        image = DCT8x8(image_to_open, Q)                                                                             
        ent2 = calculate_enthropy(image)                                                                                                                           
        image2 = iDCT8x8(image, Q)                                                                                                    
        compressed_pictures.append(image2)                                                                                                                                                                                                                                  
                                                                                           
        ent_vals.append(ent2)                                                                                                         
                                                                                                                                                                                                                                                                                                                                                   
        cR = calculate_comp_rate(org_ent, ent2, image)                                                                           
        mem = calculate_memory(ent2, image2)  
        print('\n')
        print('The entropy of the reconstructed compressed image:,', ent2)                                                                                                                         
        print('Compressionrate for compressed image:', cR)                                                                           
        print('Memory needed to store the compressed picture: in kB', mem)   

    # This part of the code is commented out, as it's supposed to save the pictures 
    # and is not need to for the to run
                                                                                                                                   
    #imageio.imsave('oblig2_oppgave2_bilde1.png', compressed_pictures[0])                                                              
    #imageio.imsave('oblig2_oppgave2_bilde2.png', compressed_pictures[1])                                                              
    #imageio.imsave('oblig2_oppgave2_bilde3.png', compressed_pictures[2])                                                              
    #imageio.imsave('oblig2_oppgave2_bilde4.png', compressed_pictures[3])                                                              
    #imageio.imsave('oblig2_oppgave2_bilde5.png', compressed_pictures[4])                                                              
                                                                                                                                                                                                                                                                         
    fig, ax = plt.subplots(2,3)                                                                                                       
                                                                                                                                      
    ax[0][0].imshow(image_to_open,cmap='gray')                                                                                        
    ax[0][1].imshow(compressed_pictures[0],cmap='gray')                                                                               
    ax[0][2].imshow(compressed_pictures[1],cmap='gray')                                                                               
    ax[1][0].imshow(compressed_pictures[2],cmap='gray')                                                                               
    ax[1][1].imshow(compressed_pictures[3],cmap='gray')                                                                               
    ax[1][2].imshow(compressed_pictures[4],cmap='gray')                                                                               
                                                                                                                                      
    ax[0][0].title.set_text('Original image: q = 0, H=7.4648')                                                                        
    ax[0][1].title.set_text(f'Compressed image, q = {q_values[0]}, H={ent_vals[0]}')                                                  
    ax[0][2].title.set_text(f'Compressed image, q = {q_values[1]}, H={ent_vals[1]}')                                                  
    ax[1][0].title.set_text(f'Compressed image, q = {q_values[2]}, H={ent_vals[2]}')                                                  
    ax[1][1].title.set_text(f'Compressed image, q = {q_values[3]}, H={ent_vals[3]}')                                                  
    ax[1][2].title.set_text(f'Compressed image, q = {q_values[4]}, H={ent_vals[4]}')                                                  
                                                                                        
                                      
    plt.show()                                                                                                                        


                                                                                                                                      
                                                                                                                                    
