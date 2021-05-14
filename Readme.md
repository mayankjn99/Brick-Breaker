Game - Smash
Terminal based game in python3 base on paddle and ball game. 
User score points with each brick is destroyed and game ends when score = 50 .



Rules of the Game -> 

To start  = > python3 main.py

Movement of the paddle - 
=> a moves paddle left 
=> d moves paddle right

=> r to release the ball 


5 types of brics red(level 1) , yellow(level 2) ,blue ( level3) , green ( fixed ) and pink ( explosive bonus one)


Power up fall  when brick breaks 
P = Paddle grab
E = Expand paddle
S = Shrink paddle
F = Fast ball 
T = Thru ball 

Lives  = 3 

USE of OOPS : 

A. Inheritance = 
3 parent class are defined  - 
1. Main = inherited by paddle and ball
2. Brick = inherited by all 5 types of bricks 
3. Power_up = inherited by all 5 power ups


B. Encapsulation = Implemented class and objects 

C. Polymorphism = render() is called in the child and parent . 


D. Abstraction = Every detail is hidden into functions for eg set speed to set speed of ball .

Level up key = U 
Or 
after scoring 30 points level 2
after scoring 60 points level 3 
Score 150 points or destroy boss enemy to finish the game
