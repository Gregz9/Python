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


# The coded is transformed into C-code by the use of numba, as it takes less time running it in C than python

# FUNTIONS/METHODS FOR USE IN TASK II
#-------------------------------------------------------------------------------------------------------------------------------------#
def DCT8x8(image, Q, q):                                                                                                              #
    image -= 128 # subtracting 128 from each pixel in the picture, thus lowering the intensity in the picture                         #
    image_DCT = np.zeros((image.shape))                                                                                               #
    for i in range(0, image.shape[0], 8):                                                                                             #
        for j in range(0, image.shape[1], 8):                                                                                         #
                                                                                                                                      #
            block_F = np.zeros((8,8)) # block for inserting new values                                                                #
            block_x = image[i:i+8, j:j+8].copy()                                                                                      #
                                                                                                                                      #
            for u in range(0, 8):                                                                                                     #
                for v in range(0, 8):                                                                                                 #
                                                                                                                                      #
                    c_u=(1/math.sqrt(2)) if u == 0 else 1                                                                             #
                    c_v=(1/math.sqrt(2)) if v == 0 else 1                                                                             #
                                                                                                                                      #
                    for x in range(0,8):                                                                                              #
                        for y in range(0, 8):                                                                                         #
                                                                                                                                      #
                            block_F[u,v] += np.cos((2*x+1)*u*np.pi/16)*np.cos((2*y+1)*v*np.pi/16)*block_x[x,y]                        #
                                                                                                                                      #
                    block_F[u,v] *= (0.25)*c_u*c_v                                                                                    #
            if q != 0:                                                                                                                #
                block_F = np.around(block_F/(q*Q), 0) # Compression performed by element-wise division by the q*Q                     #
                                                                                                                                      #
            image_DCT[i:i+8, j:j+8] = block_F                                                                                         #
    return image_DCT                                                                                                                  #
#-------------------------------------------------------------------------------------------------------------------------------------#
@jit                                                                                                                                  # 
def iDCT8x8(image):                                                                                                                   #
    f_out = np.zeros((image.shape))                                                                                                   #
                                                                                                                                      #
    for i in range(0, image.shape[0], 8):                                                                                             #
        for j in range(0, image.shape[1], 8):                                                                                         #
                                                                                                                                      #
            block = np.zeros((8,8))                                                                                                   #
            block2 = image[i:i+8, j:j+8].copy()                                                                                       #
                                                                                                                                      #
            for x in range(0, 8):                                                                                                     #
                for y in range(0, 8):                                                                                                 #
                                                                                                                                      #
                    for u in range(0,8):                                                                                              #
                        for v in range(0, 8):                                                                                         #
                            cu=(1/np.sqrt(2)) if u == 0 else 1                                                                        #
                            cv=(1/np.sqrt(2)) if v == 0 else 1                                                                        #
                            block[x,y] += np.cos((2*x+1)*u*np.pi/16)*np.cos((2*y+1)*v*np.pi/16)*cu*cv*block2[u,v]                     #
                    block[x,y] *= 0.25                                                                                                #
            f_out[i:i+8, j:j+8] =  block                                                                                              #
    return (f_out)+128                                                                                                                #
    # Comment on the output of the method                                                                                             #
#-------------------------------------------------------------------------------------------------------------------------------------#
    # After performing the division of 8x8-blocks contating the new values in cosiuns domain,                                         #
    # and then rounding them to the closest int-values, it turned out that rounding the output                                        #
    # of IDCT was corrupted. Henceforth I do not around the pixel-values in the reconstructed picture,                                #
    # but the values returned are integers.                                                                                           #
#-------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                      #
def calculate_enthropy(image):                                                                                                        #
    hist = np.zeros((256))                                                                                                            #
    image = image.clip(0, 255)                                                                                                        #
    for i in range(image.shape[0]):                                                                                                   #
        for j in range(image.shape[1]):                                                                                               #
            hist[int(image[i,j])] += 1                                                                                                #
    norm_hist = hist/(image.shape[0]*image.shape[1])                                                                                  #
    enthropy = [norm_hist[i]*np.log2(norm_hist[i]) for i in range(256) if norm_hist[i] != 0]                                          #
    enthropy = -np.sum(enthropy)                                                                                                      #
    print(enthropy)       
    # Due to the fact that a picture cannot be represented by using a decimal number of bits,
    # the enthropy value is ceiled to the closest integer value.                                                                                                             #
    return np.ceil(enthropy)                                                                                                          #
                                                                                                                                      #
@jit                                                                                                                                  #
def calculate_comp_rate(org_image_ent, new_image_ent, image):                                                                         #
    # Returns an compression rate and an estimate of the memory used by the compressed image                                                                                                                                  #
    cR = org_image_ent/new_image_ent                                                                                                  #
    mem = (image.shape[0]*image.shape[1]*new_image_ent)                                                                               #
    return cR, mem                                                                                                                    #
#-------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                      #
# MAIN-RUN SECTION OF THE CODE                                                                                                        #
#-------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                      #
if __name__ == '__main__':                                                                                                            #
    big_q = np.array([[16, 11, 10, 16, 24, 40, 51, 61],                                                                               #
                    [12, 12, 14, 19, 26, 58, 60, 55],                                                                                 #
                    [14, 13, 16, 24, 40, 57, 69, 56],                                                                                 #
                    [14, 17, 22, 29, 51, 87, 80, 62],                                                                                 #
                    [18, 22, 37, 56, 68, 109, 103, 77],                                                                               #
                    [24, 25, 55, 64, 81, 104, 113, 92],                                                                               #
                    [49, 64, 78, 87, 103, 121, 120, 101],                                                                             #
                    [72, 92, 95, 98, 112, 100, 103, 99]])                                                                             #
                                                                                                                                      #
    image_to_open = imageio.imread(sys.argv[1], as_gray=True)                                                                         #
    org_ent = calculate_enthropy(image_to_open)                                                                                       #
    q = float(sys.argv[2])                                                                                                            #
    # Those two lines of code are commented out, since I perform compression using a values og q from                                 #
    # the array below: q_values.                                                                                                      #
    #image = DCT8x8(image_to_open, big_q, q)                                                                                          #                                                                                                                                  #
    #image2 = iDCT8x8(image)                                                                                                          #
                                                                                                                                      #
    q_values = [0.1, 0.5, 2, 8, 32]                                                                                                   #
    compressed_pictures = []                                                                                                          #
    ent_vals = []                                                                                                                     #
                                                                                                                                      #
    for i in range(len(q_values)):                                                                                                    #
        image = DCT8x8(image_to_open, big_q, q_values[i])                                                                             #
                                                                                                                                      #
        image2 = iDCT8x8(image)                                                                                                       #
        compressed_pictures.append(image2)                                                                                            #
                                                                                                                                      #
        ent2 = calculate_enthropy(image2)                                                                                             #
        ent_vals.append(ent2)                                                                                                         #
                                                                                                                                      #                                                                                #                                                                                                                             #
        cR, mem = calculate_comp_rate(org_ent, ent2, image)                                                                           #
                                                                                                                                      # 
        print('Compressionrate for compressed image: ', cR)                                                                           #
        print('Memory needed to store the compressed picture:', mem)                                                                  #
                                                                                                                                      #
    imageio.imsave('oblig2_oppgave2_bilde1.png', compressed_pictures[0])                                                              #
    imageio.imsave('oblig2_oppgave2_bilde2.png', compressed_pictures[1])                                                              #
    imageio.imsave('oblig2_oppgave2_bilde3.png', compressed_pictures[2])                                                              #
    imageio.imsave('oblig2_oppgave2_bilde4.png', compressed_pictures[3])                                                              #
    imageio.imsave('oblig2_oppgave2_bilde5.png', compressed_pictures[4])                                                              #
                                                                                                                                      #
                                                                                                                                      #
    fig, ax = plt.subplots(2,3)                                                                                                       #
                                                                                                                                      #
    ax[0][0].imshow(image_to_open,cmap='gray')                                                                                        #
    ax[0][1].imshow(compressed_pictures[0],cmap='gray')                                                                               #
    ax[0][2].imshow(compressed_pictures[1],cmap='gray')                                                                               #
    ax[1][0].imshow(compressed_pictures[2],cmap='gray')                                                                               #
    ax[1][1].imshow(compressed_pictures[3],cmap='gray')                                                                               #
    ax[1][2].imshow(compressed_pictures[4],cmap='gray')                                                                               #
                                                                                                                                      #
    ax[0][0].title.set_text('Original image: q = 0, H=7.4648')                                                                        #
    ax[0][1].title.set_text(f'Compressed image, q = {q_values[0]}, H={ent_vals[0]}')                                                  #
    ax[0][2].title.set_text(f'Compressed image, q = {q_values[1]}, H={ent_vals[1]}')                                                  #
    ax[1][0].title.set_text(f'Compressed image, q = {q_values[2]}, H={ent_vals[2]}')                                                  #
    ax[1][1].title.set_text(f'Compressed image, q = {q_values[3]}, H={ent_vals[3]}')                                                  #
    ax[1][2].title.set_text(f'Compressed image, q = {q_values[4]}, H={ent_vals[4]}')                                                  #
                                                                                                                                      #
    plt.show()                                                                                                                        #
#-------------------------------------------------------------------------------------------------------------------------------------#
# DRØFTING AV KOMPRIMERINGEN:      
#-------------------------------------------------------------------------------------------------------------------------------------# 
# A) Allerede for den første verdien q=0.1 kan vi observere at bildet mister noe av kontrasten sammenlignet med 
#    originalbilde. Ved å zoome inn på bildet, er det også mulig å observere minimal glatting av de skarpeste detaljene, 
#    dvs. elementer på bildet som siden fronten av halvtaket over søylene ved inngangen til bygget. Det er også noe ringing rundt 
#    kantene til søylene, men på avstand, uten å zoome inn, ser bildene nesten like ut dersom en ser bort fra tapet i kontrast. 
#    
#    Fram til q = 8 er det svært lite forskjell mellom bildene, til tross for at entropien i bildet faller, er det først ved verdien
#    q = 8 at vi ser tydelig degradering av bildet. Vi kan se klare artefakter i form av kvadratiske strukturer i himmelen og skarpe 
#    overganger mellom disse kvadratene. Dette er selvfølgelig piksler som ikke lenger har en glatt overgang i intensitet mellom seg. 
#    Etter min mening er kan vi nå også observere svak degradering/nedbrytning av kantene på bygget i forhold til strukturene det omr-'
#    ringer i bildet. "Ringingen" i bildet blir også tydeligere. For q = 32 er bildet nesten ødelagt, de fleste detaljene er glattet og
#    brutt ned, selv når bildet blir sett på fra avstand (uten å zoome inn på). 
#
# B) Jeg mener at reksonstruksjonfeilene er "gode nok", dvs. akseptable, fram til q = 2, etter at denne verdien er passert, blir tapet i 
#    bildets strukturer og egenskaper alt for betydelig. For q = 2 ser ejg ingen kvadratiske streker på himmelen, og kantene på bildet 
#    har ennå ikke nådd en grad av degraderign som synes på avstand. 
# 
# C) Kompresjonraten øker, fordi komprimering gjør at entropien i bildet synker. Det vil si at informasjoninnholdet i bildet blir 
#    lavere, og vi trenger ikke like mange bits til å framstille intensitets-verdien, samt øker mengden av informasjon som vi fjerner 
#    fra bildet. Kompresjonraten skrives på formen CR = b/c, der b er antallet bits vi trenger for å framstille alle intensitetsverdi-
#    er i orignalbilde, mens c betegner den avrunda entropien i det komprimerte bildet som tilsvarer antallet bits. 
#    Det er da tydelig at kompresjonsraten beskriver forholdet mellom entropien i original og i det komprimerte bildet, og vil øke 
#    over tid når mer informasjon fjernes i det bildet sammenlignet med originalbilde.
#                                                                                                      
#-------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                                                      
                                                                                                                                    
