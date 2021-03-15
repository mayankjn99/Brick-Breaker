import global_var
import config
import random
from colorama import init, Fore, Back, Style

import objects

init()


class Layout():
    height = int(config.rows) 
    width = int(config.columns)
    def __init__(self):
        
        self.grid = [[" " for i in range(self.width)] for j in range(self.height)]
        self.createborderu()
        self.createborderd()  

    # print(config.level)
    def print_board(self): 
        abc = ""
        
        for y in range(1, self.height):
            pr = []
            for x in range(self.width):    
                pr.append(self.grid[y][x]+Style.RESET_ALL)
            # print(''.join(pr))
            abc += ''.join(pr)+"\n"
        print(abc)
                  


    def createborderu(self): 
        y = 4 
        for x in range(self.width):
            self.grid[y][x] = "#"
    def createborderd(self): 
        y = self.height -1 
        for x in range(self.width):
            self.grid[y][x] = "o"
