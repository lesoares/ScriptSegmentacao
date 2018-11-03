# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:58:53 2018

@author: Leticia
"""
import tkinter as tk

from PIL import ImageTk, Image
import os

path = 'C:/Users/Leticia/Documents/Trabalhos/Super resolução/Implementação/Dataset/Nova pasta/DSC_000002898.jpg'
diretorio = 'C:/Users/Leticia/Documents/Trabalhos/Super resolução/Implementação/Dataset/Nova pasta/'
fotos = os.listdir(diretorio)

root = tk.Tk()
img = ImageTk.PhotoImage(file=path)
panel = tk.Label(root, image=img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()