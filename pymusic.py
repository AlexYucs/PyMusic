import os
import random
from Tkinter import *
import pygame
from pygame import mixer
from queue import *

volume = .2
path = "C:\Users\Peihao\Desktop\MV\New folder (2)\\"
queue_forward = Queue()
stack_backward = []
current_song = ""


def back():
    global current_song
    if len(stack_backward)>0:
        queue_forward.put(current_song)
        current_song = stack_backward.pop()
        mixer.music.load(current_song) # limited mp3 support
        play1()

def stop1():
    mixer.music.pause()

def play1():
    if pygame.mixer.music.get_pos() <100:
        mixer.music.play()
    else:
        mixer.music.unpause()


def next1():
    global current_song
    if not queue_forward.empty():
        stack_backward.append(current_song)
        current_song = queue_forward.get()
        mixer.music.load(current_song) # limited mp3 support
        play1()
    else:
        stack_backward.append(current_song)
        current_song = path+random.choice(os.listdir("C:\Users\Peihao\Desktop\MV\New folder (2)"))
        mixer.music.load(current_song) # limited mp3 support
        play1()

def louder():
    global volume
    print volume
    if volume < .9:
        volume +=.1
        mixer.music.set_volume(volume)
def softer():
    global volume
    print volume
    if volume > 0.1:
        volume -=.1
        mixer.music.set_volume(volume)
def exit1():
    global window
    window.destroy()



pygame.init()
FIND_NEXT = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(FIND_NEXT)
current_song = path+random.choice(os.listdir("C:\Users\Peihao\Desktop\MV\New folder (2)"))
mixer.music.load(current_song) # limited mp3 support
mixer.music.set_volume(volume)

window = Tk()

#Label
label = Label(window, text="PyMusic")

#buttons
button_back = Button(window, text = "<<")
button_play = Button(window, text = "Play")
button_stop = Button(window, text = "Stop")
button_next = Button(window, text = ">>")
button_loud = Button(window, text = "+")
button_soft = Button(window, text = "-")
#button_exit = Button(window, text = "Exit")

label.grid(row=0,column=0,columnspan=2)
#button_exit.grid(row=0, column=1)
button_loud.grid(row=0, column=2, sticky=E+W)
button_soft.grid(row=0, column=3, sticky=E+W)

button_back.grid(row=1, column=0)
button_stop.grid(row=1, column=1)
button_play.grid(row=1, column=2)
button_next.grid(row=1, column=3)



button_back.configure(command=back)
button_stop.configure(command=stop1)
button_play.configure(command=play1)
button_next.configure(command=next1)
button_loud.configure(command=louder)
button_soft.configure(command=softer)
#button_exit.configure(command=exit1)

window.resizable(0,0)
window.attributes("-toolwindow",1)
#window.mainloop()
while True:
    window.update_idletasks()
    window.update()
    for event in pygame.event.get():
        if event.type == FIND_NEXT:
            next1()
