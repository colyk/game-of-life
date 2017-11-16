from tkinter import *
from copy import copy
from time import sleep
from random import randint
import os
import sys
from patterner import Patterner

class LifeGame():
    def __init__(self, height=5, width=5):
        self.height = height
        self.width = width
        self.new_matrix = [[0] * width for i in range(height)]
        self.old_matrix = [[0] * width for i in range(height)]

    def text_print(self):
        for i in range(self.height):
            print (("{}"*self.width).format(*self.old_matrix[i]))

    def random_fill(self):
        for i in range(self.height):
            for j in range(self.width):
                self.old_matrix[i][j] = randint(0,1)
    
    def game_not_change(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.old_matrix[i][j] != self.new_matrix[i][j]:
                    return False
        return True

    def life_cyle(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.old_matrix[i][j] == 1:
                    if self.get_neighber(i, j) == 2 or self.get_neighber(i, j) == 3:
                        self.new_matrix[i][j] = 1
                    else:
                        self.new_matrix[i][j] = 0
                else:
                    if self.get_neighber(i, j) == 3:
                        self.new_matrix[i][j] = 1
        self.old_matrix = copy(self.new_matrix)

    def life_exist(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.old_matrix[i][j] == 1:
                    return True
        return False

    def get_neighber(self, a, b):
        neighber_sum = 0
        for i in range(a - 1, a + 2):
            for j in range(b - 1, b + 2):
                if(a == i and b == j):
                    continue
                if(i < 0 or j < 0):
                    continue
                if(i > self.width - 1 or j > self.height - 1):
                    continue

                if(self.old_matrix[i][j] == 1):
                    neighber_sum += 1
        return neighber_sum

    def game(self):
        self.random_fill()
        while self.life_exist():
            os.system('cls')
            print("_"*10)
            self.text_print()
            print("_"*10)
            sleep(0.2)
            self.life_cyle()

                
if __name__ == '__main__':
    p = LifeGame()
    p.game()
