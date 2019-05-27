#!/bin/bash

import vlc
import time
import serial

p = vlc.MediaPlayer("")
baudrate = 9600
port = "/dev/ttyACM1"
doorbellSound = "sounds/vanessa_carlton_cut.mp3"


def play(songname):
    global p

    if p.is_playing():
        return

    p = vlc.MediaPlayer(songname)
    p.play()


s = serial.Serial(port=port, baudrate=baudrate)

while True:
    waiting = s.inWaiting()
    if waiting != 0:
        stuff = s.readline()
        print("ringing doorbell ...")
        play(doorbellSound)
