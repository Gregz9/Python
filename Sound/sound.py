import simpleaudio 
import numpy as np
from random import randint, random
from matplotlib import pyplot
from simpleaudio.shiny import play_buffer

def play_sound(*args): 
    sound = np.array(args).astype(np.int16)
    sound_object = simpleaudio.play_buffer(sound, 1, 2, 44100)
    sound_object.wait_done()

def random_sound(amount_seconds): 
    sound = []
    for i in range(44100 * amount_seconds): 
        sound.append(randint(0, 32000))
    
    return sound

#print(random_sound(4))

#Lyd med kvadratisk periode. Vi kan sammenligne dette med 
def series_of_waves(): 
    sound = []
    for i in range(0, 21, 2): 
        sound[50*i: 50*(i+1)+1] = [0]*50
        sound.extend([32000]*50)
    return sound

def triangle_sound(): 
    sound = []
    for i in range(0, 21, 2): 
        sound[50*i: 50*(i+1)+1] = list(range(0, 32000, (32000//50)))
        sound.extend(list(range(32000, 0, -(32000//50))))
    return sound

""" Perform a mathematical analysis of the formula for the sinusoidal wave to better understand 
 how the wave gets its shape """

def sinusoidal_sound(freqeuency, variation=44100*4): 
    """This method takes a frequency as argument whivh determines amoung of swings per second.
    Var is a secondary parameter which defines the amount of time the sound is set to play. If none 
    argument is passed, the value is set to 44100*4 sa default. This is so that we can play the sound 
    without thinking twice, or if we wish to plot the wave, just pass a different argument"""
    sound = []
    for i in range(variation): 
        sound.append(16000*(1+np.sin(freqeuency * i/44100 * 2 * np.pi)))
    return sound
    
play_sound(sinusoidal_sound(440))

pyplot.plot(sinusoidal_sound(50, 1000))
pyplot.show()

help(sinusoidal_sound)


