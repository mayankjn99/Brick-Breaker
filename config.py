import os
import sys
import termios, tty, time
from colorama import init, Fore, Back, Style
from math import pi
import numpy as np 


columns = 100
rows = 40

paddle = [[ '=','=','=','=','='],['=','=','=','=','=']]
paddle2 = [[ '=','=','=','=','=','=','='],['=','=','=','=','=','=','=']]
paddle3 = [[ '=','=','='],['=','=','=']]
shooting_paddle = [[ '=',' ',' ',' ','='],['=','=','=','=','=']]
ufo = [['^','^','^','^','^'],['|','|','|','|','|']]


ball = [['o']]
# ch = (Fore.RED + '#')
brick = [['#']]
bullet = [['!']]

Expand_paddle = [['E']]
Shrink_paddle = [['S']]
Thru_ball = [['T']]
Paddle_Grab = [['P']]
Fast_ball = [['F']]
Fire_ball = [['D']]
Bullet = [['B']]

# print(ball)