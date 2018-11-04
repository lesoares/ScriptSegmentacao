# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:58:53 2018

@author: Leticia
"""
import tkinter as tk
import tkinter.filedialog
import json
from PIL import ImageTk, Image

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
    data['pontoRecorte00'] = area[0][0]
    data['pontoRecorte01'] = area[0][1]
    data['pontoRecorte10'] = area[1][0]
    data['pontoRecorte11'] = area[1][1]

    jsonFile = open(path+'.json',"w+")
    json.dump(data, jsonFile, sort_keys = True, indent = 4, ensure_ascii = False)
    jsonFile.flush()
    jsonFile.close()



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
