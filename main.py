import numpy as np
import sys
import face_recognition
import cv2
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import *
from tkinter import filedialog

global pics


# definitions
def openFile():
    pics = filedialog.askopenfilename()

    print(pics)


# things to do
# find file in pictures
# loop over pictures in file name
# data base SQL lite

(program_name) = "Image Recognition Machine Learning Algorithm"
(defwinsize) = "450x450"
TitleOfOFD = "select pictures for processing"

win = tk.Tk()
button = Button(text=TitleOfOFD, command=openFile)
canvas = Canvas(win, width=300, height=300)
canvas.create_image(200, 200, anchor=NW, image=pics)
button.pack()
canvas.pack()

win.title(program_name)
win.geometry(defwinsize)

win.mainloop()
