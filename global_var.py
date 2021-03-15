import config 
import objects
import board
import random
from time import time

fall_brick_flag =0 
level = 1
dec_paddle=0
render_F=1
render_fb=1
fast_ball_flag=0
render_P = 1
render_bullet = 1
paddle_grab_flag=0
inc_paddle=0
expand_paddle_flag=0
shrink_paddle_flag=0
fire_ball_flag= 0
game_over =0
thru_ball_flag=0
fire_bullet_flag=0
render_S=1
render_T =1
render_E =1
ball_xcord=102
ball_ycord=34
xspeed_paddle =2
time = round(time())
time2 = 0
time3 = 0
score =0    
lives= 3
strength = [1,2,3]
mp = board.Layout()
Paddle = objects.paddle(config.paddle, 50, 35, lives)
ball = objects.Ball(config.ball,52,34)
T_ball = objects.exp_ball(config.Thru_ball,12,14)
E_paddle = objects.exp_Paddle(config.Expand_paddle,24,14)
S_paddle = objects.shrink_Paddle(config.Shrink_paddle,36,14)
P_grab = objects.paddle_grab(config.Paddle_Grab,16,14)
F_ball = objects.Fast_ball(config.Fast_ball,18,14)
D_ball = objects.Fire_ball(config.Fire_ball,20,14)
bullet = objects.Bullets(config.Bullet,40,14)
xspeed_before =0 
yspeed_before =1
l1=0
l2=0
l3=0
l4=0
thru_time_remain = 0
expand_time_remain =0 
shrink_time_remain = 0
fire_ball_time_remain =0
paddle_time_remain = 0
fire_ball_time_remain = 0
fire_bullet_time_remain =0 
arr = []
fire_arr = []
paddle_grab_flag_c=0
inc_paddle=0
expand_paddle_flag_c=0
shrink_paddle_flag_c=0
fire_ball_flag_c= 0
fire_bullet_flag_c=0
thru_ball_flag_c=0
fast_ball_flag_c=0
# brick = objects.Brick(config.brick,10,10)
brick1 = []
brick2 = []
brick3 = []
brick4 = []
brick5 = []
brick6 = []
coordinate = ()
for i in range(1,8):
    brick1.append(objects.Brick_l1(config.brick,i*5 ,12))
    coordinate=coordinate+(i*5,12,)
    brick2.append(objects.Brick_l2(config.brick,i*6,11))
    coordinate = coordinate+(i*6,11,)
    if i!=4:
        brick3.append(objects.Brick_l3(config.brick,i*9,10))
    coordinate = coordinate+(i*9,10,)
    brick4.append(objects.Brick_solid(config.brick,4*i+1,13))
    coordinate = coordinate+(4*i+1,13,)
for i in range (1,20):
    brick1.append(objects.Brick_l1(config.brick,2*(i+5),14))
    coordinate = coordinate+(2*(i*5),14,)
for i in range(36,42):
    brick5.append(objects.Special_Brick(config.brick,i,12))
    coordinate = coordinate+(i,12,)
brick2.append(objects.Brick_l2(config.brick,19,12))
brick3.append(objects.Brick_l3(config.brick,21,12))
brick6.append(objects.Rainbow_brick(config.brick,60,15))
brick6.append(objects.Rainbow_brick(config.brick,80,15))
brick6.append(objects.Rainbow_brick(config.brick,70,15))
Bricks = [brick1,brick2,brick3,brick4,brick5,brick6]


default = 0

def make_level2_bricks():
    # score+=100
    brick1 = []
    brick2 = []
    brick3 = []
    brick4 = []
    brick5 = []
    # Bricks = []
    for i in range(1,8):
            
            
            brick2.append(objects.Brick_l2(config.brick,2*i+1,11))
            if i!=2:
                brick3.append(objects.Brick_l3(config.brick,i*7,11))
            if i!=7:
                brick4.append(objects.Brick_solid(config.brick,6*i,10))
    for i in range (1,20):
        brick1.append(objects.Brick_l1(config.brick,2*(i+5),14))

    Bricks = [brick1,brick2,brick3,brick4]
    # Bricks.append(brick1)
    return Bricks

def make_level3_bricks():   
    brick1 = []
    brick2 = []
    brick3 = []
    brick4 = []
    for i in range(2,10):
        brick4.append(objects.Brick_solid(config.brick,6*i,10))
    # brick5 = []
    # # Bricks = []
    # for i in range(1,8):
            
            
    #         brick1.append(objects.Brick_l1(config.brick,2*i+1,11))
    #         if i!=2:
    #             brick3.append(objects.Brick_l3(config.brick,i*9,11))
    #         if i!=6:
    #             brick4.append(objects.Brick_solid(config.brick,6*i,10))
    # for i in range (1,25):
    #     brick2.append(objects.Brick_l2(config.brick,2*(i+5),14))
    # for i in range(10,15):
    #     brick1.append(objects.Brick_l1(config.brick,2*i+1,12))
    Bricks = [brick4]
    # Bricks.append(brick1)
    return Bricks 