# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:58:53 2018

@author: Leticia
"""
import tkinter as tk
import tkinter.filedialog
from PIL import ImageTk, Image

# Controla os clicks do mouse e a criação dos retângulos de seleção
def mouse_control(event):
    global area

    # Corrige as coordenadas de acordo com as Scrollbars
    xpos = event.x + x_scroll.get()[0] * xres
    ypos = event.y + y_scroll.get()[0] * yres

    # Coordenadas guardadas em uma lista de tuplas
    # Guarda apenas as coordenadas do último retângulo
    if(str(event.type) == 'ButtonPress'):
        area = [(xpos, ypos)]

    elif(str(event.type) == 'ButtonRelease'):
        area.append((xpos, ypos))
        panel.create_rectangle(area[0][0], area[0][1], area[1][0], area[1][1],
                                width = 2, outline = "#00FF00")


# Limpa panel e carrega a imagem selecionada nele
def select_click():
    path = tkinter.filedialog.askopenfilename(initialdir="G:/Meu Drive/Imagens Uteis")
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

panel.bind("<ButtonPress-1>", mouse_control)
panel.bind("<ButtonRelease-1>", mouse_control)

root.mainloop()
