import numpy as np 
import matplotlib.pyplot as plt 
import imageio 
import math 
import time 
from numpy.fft import fft2 
from scipy import signal
import cv2 
import matplotlib as mb

# Task 1.1

image_cow = imageio.imread('cow.png', as_gray=True)
cow_array = np.array(image_cow)
cow_fft = np.fft.fftshift(fft2(image_cow))

# SPATIAL DOMAIN FILTERING
#--------------------------------------------------------------------------------------#
mid_filter_spatial = np.ones((15,15))*(1/15**2)

spatial_cow = signal.convolve2d(image_cow, mid_filter_spatial, mode='same')

plt.show()
#--------------------------------------------------------------------------------------#

# FREQUENCY DOMAIN FILTERING
#--------------------------------------------------------------------------------------#

mid_filter_padded = np.zeros((image_cow.shape))
mid_filter_padded[377:392, 513:528] = mid_filter_spatial
mid_filter_frequency = np.fft.fftshift(fft2(mid_filter_padded))


phase  = np.angle(cow_fft)
magnitude = np.abs(cow_fft)
spectrum = np.log(abs(cow_fft))

cow_conv_freq = np.multiply(cow_fft, mid_filter_frequency)

ifft_image = np.fft.ifft2((cow_conv_freq))
ifft_image = np.fft.ifftshift(ifft_image)
ifft_image2 = np.abs(ifft_image)
#--------------------------------------------------------------------------------------#

mid_filter_frequency = np.fft.fftshift((fft2(mid_filter_spatial,(768, 1024))))
cow_conv_freq = np.multiply(cow_fft, mid_filter_frequency)
return_image = np.fft.ifft2(cow_conv_freq)
ifft_image = np.abs(return_image)

fig, ax = plt.subplots(1,3)

ax[0].imshow(image_cow,cmap='gray',vmin=0,vmax=255,aspect='auto')
ax[1].imshow(spatial_cow,cmap='gray',vmin=0,vmax=255,aspect='auto')
ax[2].imshow(ifft_image,cmap='gray',vmin=0,vmax=255,aspect='auto')

ax[0].title.set_text('Original image')
ax[1].title.set_text('Spatial domain filtering')
ax[2].title.set_text('Frequency domain filtering')

plt.show()  

# COMMENTS ON RESULTS - Task 1.2
#--------------------------------------------------------------------------------------#

"""
I.  Lowpass filtering using a mean filter when filtering in the spatial domain yields a 
    picture containig dark borders. This is a result of using zero-padding on the borders, 
    which results in lower values along the edges of the image. These phenomena is caused by
    calculating the intensity of each pixel as a sum of 15**2 pixels multiplied by 1/(15**2), 
    and as such results in lower intesity values along the edges where most of the zeros 
    recide. 

II. When filtering in the frequency domain, the resulting picture has an odd thin upper edge. 
    Looking closer it resembles the lower part of the our picture, but how can that be? Well, as 
    it turns out that tranforming the picture and the filter kernel/function from spatial to 
    frequency domain introduces periodicity (implicit). This results from the fact that the 
    Discrete Fourier Transform of a function (image or filter kernel) is a sum of sines and cosines 
    needed to aproximate the shape of the sampled functions in frequency domain. However all cosines 
    and sines are continuous functions that swing with a given frequency. Thus a ''discontinuity''/wrap-
    around of the bottom part of the picture in its upper edge. 
    
"""
#--------------------------------------------------------------------------------------#
# Task 1.3 

filter_sizes = [1, 3, 5, 10, 15, 25, 50, 100]
spatial_filters = []

for i in range(len(filter_sizes)): 
    size = filter_sizes[i]
    spatial_filters.append(np.ones((size, size))*(1/size**2))

frequency_filters = []
for j in range(len(spatial_filters)): 
    kernel = spatial_filters[j]
    frequency_filters.append(np.fft.fftshift(fft2(kernel,(image_cow.shape[0],image_cow.shape[1]))))

spatial_times = []
for k in range(len(spatial_filters)): 
    start_time = time.time()
    spatial_image = signal.convolve2d(image_cow, spatial_filters[k], mode='same')
    end_time = (time.time()-start_time)
    spatial_times.append(end_time)

# Time has been measured for the situation where bringing the spatial filter into frequency domain was 
# included in the convolution, however no discernible difference was observed, and thus the transformation 
# of the spatial filter into a frequency domain filter is excluded, as we're simply concerned about the time of 
# the convolution.
frequency_times = []
for l in range(len(frequency_filters)): 
    start_time = time.time() 
    frequency_image = np.multiply(cow_fft, frequency_filters[l])
    frequency_image = np.fft.ifft2(frequency_image)
    frequency_image = np.abs(frequency_image)
    end_time = (time.time()-start_time)
    frequency_times.append(end_time)

plt.plot([i for i in filter_sizes], spatial_times, 'b', label='Convlution time in the spatial domain')
plt.plot([i for i in filter_sizes], frequency_times, 'g', label='Convlution time in the frequency domain')
plt.legend()
plt.show()


# COMMENTS - TASK 1.3
#--------------------------------------------------------------------------------------#
"""
I.  When looking at the curves of time measured for convolution using a mean-value filter, 
    after passing the size of kernel of size 4 in the spatial domain, bringing the filters 
    to the frequency domain gives a visible time advantage, especially when the kernel-size 
    of 6*6 is passed in the spatial domain. I had some concerns in the beggining, as
    the time for the DFT-transofrm filtering does not increase visibly. When I checked the 
    results of the filtering however, everything was working just fine. The conclucion is hence
    that there's a clear advantage in bringing the image and the filter to the frequency domain for 
    filter-sizes above 4*4. The advantage comes from the fact that filtering in the frequnecy domain 
    depends on us always padding the filter transfer function to match the dimension/size of the 
    picture we're about to filter. Thus we always keep the size of the filter constant. One last 
    thing to consider is the fact that when we convolve in the spatial domain, we multiply element-wise
    in hte frequency domain, and do not have to extract a neighbourhood for each pixel the program is 
    standing at. 

"""