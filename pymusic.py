 # -*- coding: utf-8 -*-
import os
import random
from Tkinter import *
import pygame
from pygame import mixer
from queue import *

volume = .1
path = os.getcwd()+"\Music\\"
queue_forward = Queue()
stack_backward = []
current_song = ""

#last song
def back():
    global current_song
    if len(stack_backward)>0:
        queue_forward.put(current_song)
        current_song = stack_backward.pop()
        mixer.music.load(current_song) # limited mp3 support
        mixer.music.play()
        print "Playing: "+current_song
    else:
        print "Stack is Empty"

#play pause
def stop1():
    mixer.music.pause()
def play1():
    if pygame.mixer.music.get_pos() <100:
        mixer.music.play()
    else:
        mixer.music.unpause()

#next song
def next1():
    global current_song
    if not queue_forward.empty():
        stack_backward.append(current_song)
        current_song = queue_forward.get()
        mixer.music.load(current_song) # limited mp3 support
        mixer.music.play()
    else:
        stack_backward.append(current_song)
        current_song = path+random.choice(os.listdir(path))
        mixer.music.load(current_song) # limited mp3 support
        mixer.music.play()
    print "Playing: "+current_song

#volume controls
def louder():
    global volume
    if volume < .9:
        volume +=.1
        mixer.music.set_volume(volume)
    print "Volume: ",
    print volume
def softer():
    global volume
    if volume >= 0.1:
        volume -=.1
        mixer.music.set_volume(volume)
    else:
        volume=0
        mixer.music.set_volume(volume)
    print "Volume: ",
    print volume

#Exit
def exit1():
    global window
    window.destroy()

class WindowDraggable():

    def __init__(self, label):
        self.label = label
        label.bind('<ButtonPress-1>', self.StartMove)
        label.bind('<ButtonRelease-1>', self.StopMove)
        label.bind('<B1-Motion>', self.OnMotion)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self,event):
        x = (event.x_root - self.x - self.label.winfo_rootx() + self.label.winfo_rootx())
        y = (event.y_root - self.y - self.label.winfo_rooty() + self.label.winfo_rooty())
        window.geometry("+%s+%s" % (x, y))


pygame.init()
FIND_NEXT = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(FIND_NEXT)
current_song = path+random.choice(os.listdir(path))
mixer.music.load(current_song) # limited mp3 support
mixer.music.set_volume(volume)

window = Tk()

#Label
label = Label(window, text="Py♫")
WindowDraggable(label)

#buttons
button_back = Button(window, text = "<<")
button_play = Button(window, text = "Play")
button_stop = Button(window, text = "Stop")
button_next = Button(window, text = ">>")
button_loud = Button(window, text = "+")
button_soft = Button(window, text = "-")
button_exit = Button(window, text = "Exit")

#row 0
label.grid(row=0,column=0,sticky=E+W)
button_exit.grid(row=0, column=1, sticky=E+W)
button_loud.grid(row=0, column=2, sticky=E+W)
button_soft.grid(row=0, column=3, sticky=E+W)

#row 1
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
button_exit.configure(command=exit1)
window.overrideredirect(1)

window.resizable(0,0)
window.attributes("-topmost",1)

#replace mainloop()
while True:
    window.update_idletasks()
    window.update()
    for event in pygame.event.get():
        if event.type == FIND_NEXT:
            next1()
