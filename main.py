import numpy as np
import sys
import face_recognition
import cv2
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import *
from tkinter import filedialog


# definitions
def openFile():
    Tpngs: object = filedialog.askopenfilename()
    print(Tpngs)


# things to do
# find file in pictures
# loop over pictures in file name
# data base SQL lite

img = cv2.imread('Tpngs', 1)

(program_name) = "Image Recognition Machine Learning Algorithm"
(defwinsize) = "450x450"
TitleOfOFD = "select PNGs for processing"
win = tk.Tk()
button = Button(text=TitleOfOFD, command=openFile)

win.title(program_name)
win.geometry(defwinsize)
button.pack()
win.mainloop()
