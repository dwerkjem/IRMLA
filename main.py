import torch
import numpy as np
import torchvision
import sys
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import *
from tkinter import filedialog


def openFile():
    PNGs = filedialog.askopenfilename()
    print(PNGs)


(program_name) = "Image Recognition Machine Learning Algorithm"
(defwinsize) = "450x450"
initaldir = "C:"
TitleOfOFD = "select PNGs for processing"
filetypes = "pngs" "*.png"
win = tk.Tk()
button = Button(text=TitleOfOFD, command=openFile)

win.title(program_name)
win.geometry(defwinsize)
button.pack()
win.mainloop()
