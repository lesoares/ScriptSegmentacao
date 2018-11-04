# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:58:53 2018

@author: Leticia
"""
import tkinter as tk
import tkinter.filedialog
import json
from PIL import ImageTk, Image

def crop_image():
    img = Image.open(path)
    cropped_image = img.crop((area[0][0],area[0][1],area[1][0],area[1][1]))
    nome_imagem = path[:-4]
    cropped_image.save(nome_imagem+'_cropped.jpg', "JPEG")

def mouse_pressed(event):
    global area

    xpos = event.x + x_scroll.get()[0] * xres
    ypos = event.y + y_scroll.get()[0] * yres

    area = [[xpos, ypos]]


def mouse_released(event):
    xpos = event.x + x_scroll.get()[0] * xres
    ypos = event.y + y_scroll.get()[0] * yres

    area.append([xpos, ypos])

    area[0][0], area[1][0] = min(area[0][0], area[1][0]), max(area[0][0], area[1][0])
    area[0][1], area[1][1] = min(area[0][1], area[1][1]), max(area[0][1], area[1][1])

    panel.create_rectangle(area[0][0], area[0][1], area[1][0], area[1][1],
                            width = 2, outline = "#00FF00")
    
    print('x'+path)
    data = {}
    data['imageName'] = path
    data['pontoRecorteX1'] = area[0][0]
    data['pontoRecorteY1'] = area[0][1]
    data['pontoRecorteX2'] = area[1][0]
    data['pontoRecorteY2'] = area[1][1]

    jsonFile = open(path+'_cropped'+'.json',"w+")
    json.dump(data, jsonFile, sort_keys = True, indent = 4, ensure_ascii = False)
    jsonFile.flush()
    jsonFile.close()
    crop_image()


def select_click():
    global path
    path = tkinter.filedialog.askopenfilename(initialdir="../Dataset/Nova_pasta/")
    if(len(path) > 0):
        panel.delete("all")
        img = ImageTk.PhotoImage(file=path)
        panel.img = img
        panel.create_image(0, 0, image=img, anchor='nw')


area = []
xres, yres = 6000, 4000

root = tk.Tk()
root.title("Segmentação Manual")

select_btn = tk.Button(root, text = "Selecionar Imagem", command = select_click)
select_btn.pack(side = "top")

y_scroll = tk.Scrollbar(root, orient = "vertical")
y_scroll.pack(side = "right", fill = "y")
x_scroll = tk.Scrollbar(root, orient = "horizontal")
x_scroll.pack(side = "bottom", fill= "x")

panel = tk.Canvas(root, width = 1800, height = 1000,
                    yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set,
                    scrollregion=(0, 0, xres, yres))
panel.pack(side = "bottom", fill = "x", expand = "yes")

y_scroll.config(command = panel.yview)
x_scroll.config(command = panel.xview)

panel.bind("<ButtonPress-1>", mouse_pressed)
panel.bind("<ButtonRelease-1>", mouse_released)
panel.bind()

root.mainloop()
