import os
import random
import Tkinter
import vlc

current_song = current_song = vlc.MediaPlayer(random.choice(os.listdir(path)))

def stop1():
    current_song.stop()

def play1():
    current_song.play()

def next1():
    current_song = current_song = vlc.MediaPlayer(random.choice(os.listdir(path)))
    play1()


window = Tk()
button_play = Button(window, text = "Play")
button_stop = Button(window, text = "Stop")
button_next = Button(window, text = "Next")


button_stop.pack(side=LEFT)
button_play.pack(side=LEFT)
button_next.pack(side=LEFT)

button_stop.configure(command=stop1)
button_play.configure(command=play1)
button_next.configure(command=next1)
