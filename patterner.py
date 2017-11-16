#!/usr/bin/python3

from tkinter import *
from random import randint
import time  #убрать для модуля

class Patterner:
    def __init__(self, matrix, pixel_size = 1, mode = 'wb'):
        #Modes: "wb", "color"
        self.p_size = pixel_size
        self.mode = mode
        self.tk = Tk()
        self.set_matrix(matrix)
        self.create_canvas(self.c_size)
        self.tk.geometry('{}x{}+100+100'.format(100,100)) 
        self.tk.resizable(False, False)

    def set_matrix(self, m):
        self.matrix = m
        self.c_size = len(self.matrix) * self.p_size + 1
        self.rng = range(0, len(self.matrix))

    def set_mode(self, mode):
        self.mode = mode

    def clean(self):
        self.tk.destroy()
        
    def create_canvas(self, size):
        self.c = Canvas(self.tk, width=size, height=size)
        self.c.pack()

    def draw(self):
        x0, y0, x1, y1 = 0, 0, self.p_size, self.p_size

        for i in self.rng:
            for ii in self.rng:
                if (self.mode == 'color'):
                    clr = self.matrix[i][ii]
                elif (self.mode == 'wb'):
                    if (self.matrix[i][ii] == 1):
                        clr = 'black'
                    else: 
                        clr = 'white'

                self.c.create_rectangle(x0, y0, x1, y1, fill = clr, width = 0)
                x0 += self.p_size
                x1 += self.p_size
            x0 = 0
            y0 += self.p_size
            x1 = self.p_size
            y1 += self.p_size
        self.tk.update_idletasks()
        self.tk.update()
        

    def bind(self, key, event):
        self.tk.bind(key, event)

def rnd_matrix(n):
    return [[randint(0,1) for x in range(n)] for xx in range(n)]

def rnd_color():
    ch = ['a','b','c','d','e','f']
    clr = '#'
    for i in range(6):
        x = randint(0,100)
        if(x < 50):
            clr += ch[randint(0,5)]
        else:
            clr += str(randint(0,9))
    return clr

def rnd_matrix_c(n):
    return [[rnd_color() for x in range(n)] for xx in range(n)]


if __name__ == '__main__':
    m = rnd_matrix_c(20)
    p = Patterner(m, 20, 'color')
    print(p)
    p.draw()
    time.sleep(2)
    p.clean()
    p.set_mode('wb')
    p.set_matrix(rnd_matrix(20))
    p.draw()
    
    input()