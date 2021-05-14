import global_var 
import config
from time import time,sleep
import random
from colorama import  Fore, Back, Style 
import colorama
# from playsound import playsound
colorama.init() 


class Main():
    
    def __init__(self, feature, x, y):
        self.xcord = x
        self.ycord = y
        self.width = len(feature[0])
        self.height = len(feature)
        self.shape = feature
    
    def moveleft(self,x):
        if self.xcord >=3:
            self.xcord+=x
    def moveleftball(self,x):
        if self.xcord >=5:
            self.xcord+=x
        
    def moverightball(self,x):
        if self.xcord <=93:
            self.xcord+=x
    def moveright(self,x):
        if self.xcord <= 91:
            self.xcord+=x
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                # print("Hi   ")
                global_var.mp.grid[j+self.ycord][i+self.xcord] = self.shape[j][i]
    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = " "


class paddle(Main):
    def __init__(self, feature,x, y, lives):
        super().__init__(feature, x, y)
        self.lives = 3 
        # self.arr   = [self.xcord,self.xcord+1,self.xcord+2,self.xcord+3,self.xcord+4]
        
    def current_x():
        return self.xcord
    
    def current_y():
        return self.ycord
    def lives(self):
        return self.lives

    def render(self):

        if global_var.expand_paddle_flag==1:
            # print("HI")
            self.shape=config.paddle2

            self.width=len(config.paddle2[0])


        if global_var.shrink_paddle_flag==1:
            self.shape=config.paddle3
            self.width=len(config.paddle3[0])
        elif global_var.shrink_paddle_flag==0 and global_var.expand_paddle_flag==0:
            self.shape=config.paddle
            self.width=len(config.paddle[0])
            if global_var.fire_bullet_flag ==1:
                self.shape=config.shooting_paddle

                self.width=len(config.shooting_paddle[0])
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = self.shape[j][i]

class Ball(Main):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.xspeed=0
        self.yspeed=0
    
    def render_collision(self):
        for i in global_var.Bricks:
            for j in i:
                j.render()
                j.collision()
        for i in global_var.enemybricks:
            for j in i:
                j.render()
                j.collision()
    def set_speed(self):
        if self.yspeed == 0 :
            self.yspeed=global_var.yspeed_before
        if self.xspeed == 0:
            self.xspeed =global_var.xspeed_before 

    def detect_collision(self):
        if self.xcord <= 1 :
            self.xspeed*=-1
        elif self.xcord + self.xspeed>=96:
            self.xspeed*=-1
        if self.ycord <=6:
            self.yspeed*=-1
        elif self.ycord >=38:
            reset()
            # self.yspeed*=-1
    # def detect_collision_brick():


    def render(self):
        self.detect_collision()
        # self.detect_collision_brick()
        if self.ycord == 35 :
            # arr   = [global_var.Paddle.xcord,global_var.Paddle.xcord+1,global_var.Paddle.xcord+2,global_var.Paddle.xcord+3,global_var.Paddle.xcord+4]
            for i in range(global_var.Paddle.width):
                value= global_var.Paddle.xcord+i
                if self.xcord ==value:
                    # playsound('41089882_drink-glass-breaking-01.mp3')
                    if global_var.paddle_grab_flag==1:
                        self.ycord=34
                        # self.xspeed=2
                        global_var.xspeed_before= self.xspeed
                        global_var.yspeed_before=self.yspeed*-1
                        self.xspeed=0
                        self.yspeed=0
                        global_var.default=0
                    else:
                        self.yspeed*=-1
                        if global_var.Paddle.width==5:
                            self.xspeed+= i-2
                        elif global_var.Paddle.width==3:
                            self.xspeed+=i-1
                        elif global_var.Paddle.width==7:
                            self.xspeed+=i-3
                    if global_var.fall_brick_flag==1:
                        for i in global_var.Bricks:
                            for j in i:
                                j.down()  
                        for i in global_var.enemybricks:
                            for j in i:
                                j.down()         
                        if global_var.thru_ball_flag_c==0:        
                            global_var.T_ball.down()
                        if global_var.expand_paddle_flag_c==0:
                            global_var.E_paddle.down()
                        if global_var.shrink_paddle_flag_c==0:
                            global_var.S_paddle.down()
                        if global_var.paddle_grab_flag_c==0:
                            global_var.P_grab.down()        
                        if global_var.fast_ball_flag_c==0:
                            global_var.F_ball.down()        
                        if global_var.fire_ball_flag_c==0:
                            global_var.D_ball.down()
                        if global_var.fire_bullet_flag_c==0:
                            global_var.bullet.down()  

        if self.ycord == 7:
            for i in range(global_var.Enemy.width):
                value= global_var.Enemy.xcord+i
                if self.xcord ==value:  
                    global_var.Enemy.lives-=1
                    global_var.ball.yspeed*=-1                   

        self.ycord-=self.yspeed
        self.xcord+=self.xspeed
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = self.shape[j][i]


       
        

def reset():
   
    # global_var.ball.clear()
    global_var.Paddle.clear()
    global_var.thru_ball_flag=0
    global_var.expand_paddle_flag=0
    global_var.shrink_paddle_flag=0
    global_var.paddle_grab_flag=0
    global_var.fast_ball_flag=0
    global_var.fire_ball_flag=0
    global_var.fire_bullet_flag=0

    global_var.Paddle = paddle(config.paddle, 50, 35, global_var.lives-1)
    global_var.lives-=1
    # global_var.ball.clear()
    global_var.ball = Ball(config.ball,52,34)
    global_var.ball.xspeed =0 
    global_var.ball.yspeed = 0
    global_var.default = 0
 


class Brick():
    def __init__(self, feature, x, y):
        self.xcord = x
        self.ycord = y
        self.speed = 1
        self.shape = feature
        self.width = len(feature[0])
        self.height = len(feature)
    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = " "
    
    # def down(self):
    #     self.clear()
    #     self.ycord+=1


class Brick_l1(Brick):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.strength=1

  
    def collision(self):
        if global_var.level == 1 and (self.xcord,self.ycord) in global_var.arr and self.strength >0:
            self.strength=0
            if global_var.l1==0:
                global_var.score+=1
                global_var.l1=1 
        elif global_var.level == 1 and (self.xcord,self.ycord) in global_var.fire_arr and self.strength >0:
            self.strength=0
            if self.xcord==12 and global_var.level !=3:
                if global_var.render_T == 1:
                    global_var.render_T=0
                global_var.thru_ball_flag_c=1
                global_var.T_ball.ycord-=2
                global_var.T_ball.xspeed = global_var.ball.xspeed               
            elif self.xcord ==24  and global_var.level ==1 :
                global_var.render_E=0
                global_var.expand_paddle_flag_c=1
                global_var.E_paddle.ycord-=2
                global_var.E_paddle.xspeed = global_var.ball.xspeed                
            elif self.xcord==36 and global_var.level !=3:
                global_var.render_S=0 
                global_var.shrink_paddle_flag_c=1
                global_var.S_paddle.ycord-=2
                global_var.S_paddle.xspeed = global_var.ball.xspeed   
            elif self.xcord == 16 and  global_var.level !=3:
                global_var.render_P=0  
                global_var.paddle_grab_flag_c=1
                global_var.P_grab.ycord-=2
                global_var.P_grab.xspeed = global_var.ball.xspeed   
            elif self.xcord == 18 and global_var.level ==1  and  global_var.level !=3:
                global_var.render_F=0
                global_var.fast_ball_flag_c=1
                global_var.F_ball.ycord-=2
                global_var.F_ball.xspeed = global_var.ball.xspeed  
            elif self.xcord == 20  and global_var.level ==1  and  global_var.level !=3:
                global_var.render_fb= 0
                global_var.fire_ball_flag_c=1
                global_var.D_ball.ycord-=2
                global_var.D_ball.xspeed = global_var.ball.xspeed    
            elif self.xcord == 40  and  global_var.level !=3:
                global_var.render_bullet =0
                global_var.fire_bullet_flag_c=1
                global_var.bullet.ycord-=2
                global_var.bullet.xspeed = global_var.ball.xspeed                          
                
        elif self.strength >0 :
            if self.xcord == global_var.ball.xcord and self.ycord == global_var.ball.ycord:
                if global_var.thru_ball_flag ==1:
                    self.strength=0
                    global_var.score+=1
                    
                
                elif global_var.fire_ball_flag == 1:
                    if global_var.thru_ball_flag == 0:
                        self.strength=0
                        global_var.score+=1
                        global_var.ball.yspeed*=-1
                    fire_with_fire(self.xcord,self.ycord)
                    


                else:
                    # print("Hi")

                    self.strength-=1
                    if self.strength ==0:
                        global_var.score+=1
                        
                    global_var.ball.yspeed*=-1

                if self.xcord==12  and  global_var.level !=3:
                    if global_var.render_T == 1:
                        global_var.render_T=0
                    global_var.thru_ball_flag_c=1
                    global_var.T_ball.ycord-=2
                    global_var.T_ball.xspeed = global_var.ball.xspeed
                elif self.xcord ==24 and global_var.level ==1 :
                    global_var.render_E=0
                    global_var.expand_paddle_flag_c=1
                    global_var.E_paddle.ycord-=2
                    global_var.E_paddle.xspeed = global_var.ball.xspeed
                elif self.xcord==36  and  global_var.level !=3:
                    global_var.render_S=0 
                    global_var.shrink_paddle_flag_c=1
                    global_var.S_paddle.ycord-=2
                    global_var.S_paddle.xspeed = global_var.ball.xspeed                    
                elif self.xcord == 16  and  global_var.level !=3:
                    global_var.render_P=0  
                    global_var.paddle_grab_flag_c=1
                    global_var.P_grab.ycord-=2
                    global_var.P_grab.xspeed = global_var.ball.xspeed                    
                elif self.xcord == 18 and global_var.level ==1:
                    global_var.render_F=0
                    global_var.fast_ball_flag_c=1
                    global_var.F_ball.ycord-=2
                    global_var.F_ball.xspeed = global_var.ball.xspeed                        
                elif self.xcord == 20  and global_var.level ==1:
                    global_var.render_fb= 0
                    global_var.fire_ball_flag_c=1
                    global_var.D_ball.ycord-=2
                    global_var.D_ball.xspeed = global_var.ball.xspeed                                           
                  
                
                elif self.xcord == 40  and  global_var.level !=3:
                    global_var.render_bullet =0
                    global_var.fire_bullet_flag_c =1
                    global_var.bullet.ycord-=2
                    global_var.bullet.xspeed = global_var.ball.xspeed                          
            elif global_var.fire_bullet_flag==1 :
                if self.xcord == global_var.fire_bullet.xcord and self.ycord == global_var.fire_bullet.ycord:
                    self.strength-=1
                    global_var.fire_bullet.xcord=global_var.Paddle.xcord
                    global_var.fire_bullet.ycord=global_var.Paddle.ycord

    def down(self):
        self.clear()
        if self.strength !=0 and self.ycord >=34:
            global_var.game_over =1  
        self.ycord+=1

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.strength==1:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.RED+self.shape[j][i])
                elif self.strength==0:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = " "

class Brick_l2(Brick):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.strength=2
    def collision(self):
        if global_var.level == 1 and (self.xcord,self.ycord) in global_var.arr:
            self.strength=0
            if global_var.l2==0:
                global_var.score+=4
                global_var.l2=1
        elif global_var.level == 1 and (self.xcord,self.ycord) in global_var.fire_arr:
            self.strength=0
        elif self.strength >=1 :
            if self.xcord == global_var.ball.xcord and self.ycord == global_var.ball.ycord:
                if global_var.thru_ball_flag ==1:
                    self.strength=0
                    global_var.score+=2
                elif global_var.fire_ball_flag == 1:
                    if global_var.thru_ball_flag == 0:
                        self.strength=0
                        global_var.score+=2
                        global_var.ball.yspeed*=-1
                    fire_with_fire(self.xcord,self.ycord)
                else:
                    self.strength-=1
                    if self.strength ==0:
                        global_var.score+=2
                    global_var.ball.yspeed*=-1
            elif global_var.fire_bullet_flag==1 :
                if self.xcord == global_var.fire_bullet.xcord and self.ycord == global_var.fire_bullet.ycord:
                    self.strength-=1
                    global_var.fire_bullet.xcord=global_var.Paddle.xcord
                    global_var.fire_bullet.ycord=global_var.Paddle.ycord
    def down(self):
        self.clear()
        if self.strength !=0 and self.ycord >=34:
            global_var.game_over =1  
        self.ycord+=1    
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.strength==2:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.YELLOW+self.shape[j][i])
                elif self.strength==1:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.RED+self.shape[j][i])
                elif self.strength==0:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = " "

class Brick_l3(Brick):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)   
        self.strength=3
    def collision(self):
        if global_var.level == 1 and (self.xcord,self.ycord) in global_var.arr:
            self.strength=0
            if global_var.l3==0:
                global_var.score+=3
                global_var.l3=1
        elif global_var.level == 1 and (self.xcord,self.ycord) in global_var.fire_arr:
            self.strength=0
        elif self.strength >=1 :
            if self.xcord == global_var.ball.xcord and self.ycord == global_var.ball.ycord:
                if global_var.thru_ball_flag ==1:
                    self.strength=0
                    global_var.score+=3
                elif global_var.fire_ball_flag == 1:
                    if global_var.thru_ball_flag == 0:
                        self.strength=0
                        global_var.score+=3
                        global_var.ball.yspeed*=-1
                    fire_with_fire(self.xcord,self.ycord)
                else:
                    self.strength-=1
                    if self.strength ==0:
                        global_var.score+=3
                    global_var.ball.yspeed*=-1
            elif global_var.fire_bullet_flag==1 :
                if self.xcord == global_var.fire_bullet.xcord and self.ycord == global_var.fire_bullet.ycord:
                    self.strength-=1
                    global_var.fire_bullet.xcord=global_var.Paddle.xcord
                    global_var.fire_bullet.ycord=global_var.Paddle.ycord                    
    def down(self):
        self.clear()
        if self.strength !=0 and self.ycord >=34:
            global_var.game_over =1  
        self.ycord+=1
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.strength==3:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.BLUE+self.shape[j][i])
                elif self.strength==2:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.YELLOW+self.shape[j][i])
                elif self.strength==1:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.RED+self.shape[j][i])
                elif self.strength==0:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = " "
    
class Brick_solid(Brick):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.strength=100

    def collision(self):
        if global_var.level == 1 and (self.xcord,self.ycord) in global_var.arr:
            self.strength=0
            if global_var.l4==0:
                global_var.score+=4
                global_var.l4=1
        elif global_var.level == 1 and (self.xcord,self.ycord) in global_var.fire_arr:
            self.strength=0
        elif self.strength >=1 :
            if self.xcord == global_var.ball.xcord and self.ycord == global_var.ball.ycord:
                if global_var.thru_ball_flag ==1:
                    self.strength=0
                elif global_var.fire_ball_flag == 1:
                    if global_var.thru_ball_flag == 0:
                        self.strength=0
                        # global_var.score+=1
                        # global_var.ball.yspeed*=-1
                    fire_with_fire(self.xcord,self.ycord)
                else:
                    global_var.ball.yspeed*=-1
    def down(self):
        self.clear()
        if self.strength !=0 and self.ycord >=34 :
            global_var.game_over =1  
        self.ycord+=1                    
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.strength==0:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = " "
                else :
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.GREEN+self.shape[j][i])

class Special_Brick(Brick):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.strength=1

    def collision(self):
        if (self.xcord,self.ycord) in global_var.arr:
            self.strength=0
            # global_var.score+=1
            Deal_Exposion(self.xcord,self.ycord)
        elif self.strength >=1 :
            if self.xcord == global_var.ball.xcord and self.ycord == global_var.ball.ycord:
                    
                    global_var.ball.yspeed*=-1
                    self.strength=0
                    # global_var.score+=1
                    Deal_Exposion(self.xcord,self.ycord)
    def down(self):
        self.clear()
        if self.strength !=0 and self.ycord >=35:
            global_var.game_over =1  
        self.ycord+=1                
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.strength==0:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = " "
                else :
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.MAGENTA+self.shape[j][i])
    
class Rainbow_brick(Brick):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.strength=3
        self.collision_happened=0
    def down(self):
        self.clear()
        if self.strength !=0 and self.ycord >=35:
            global_var.game_over =1  
        self.ycord+=1    
    def collision(self):
        if self.xcord == global_var.ball.xcord and self.ycord == global_var.ball.ycord:
            if self.strength>0:
                global_var.ball.yspeed*=-1
            self.collision_happened=1
            self.strength -=1
            # self.strength=0
                    # global_var.score+=1
                    # Deal_Exposion(self.xcord,self.ycord)                
    def render(self):
        if self.collision_happened==0:
            self.strength = random.randint(1,3)
        
        for i in range(self.width):
            for j in range(self.height):
                if self.strength==3:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.BLUE+self.shape[j][i])
                elif self.strength==2:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.YELLOW+self.shape[j][i])
                elif self.strength==1:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.RED+self.shape[j][i])
                elif self.strength==0:
                    global_var.mp.grid[j+self.ycord][i+self.xcord] = " "   
class Power_up():
    def __init__(self, feature, x, y):
        self.xcord = x
        self.ycord = y
        self.width = len(feature[0])
        self.height = len(feature)
        self.shape = feature
    
    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = " "
    
    def down(self):
        if self.ycord <= 36:
            self.ycord +=1

        
class exp_ball(Power_up):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.yspeed=1
        self.xspeed= -1
    
    def wall_collision(self):
        if self.ycord >=37:
            global_var.render_T =1
    
    def paddle_collision(self):
        if self.ycord==35:
            # arr = [global_var.Paddle.xcord,global_var.Paddle.xcord+1,global_var.Paddle.xcord+2,global_var.Paddle.xcord+3,global_var.Paddle.xcord+4]
            for i in range(global_var.Paddle.width):
                value= global_var.Paddle.xcord+i
                if self.xcord == value:
                    global_var.render_T =1
                    global_var.thru_ball_flag=1
                    global_var.thru_time_remain=round(time())+15
                    self.shape=[[' ']]

    def render(self):
        if self.ycord + self.yspeed <=38:
            self.ycord+=self.yspeed
        if self.xcord + self.xspeed<=2 :
            self.xspeed*=-1
        if self.xcord + self.xspeed>=95:
            self.xspeed*=-1
        self.xcord+=self.xspeed
        self.paddle_collision() 
        self.wall_collision()
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.GREEN+self.shape[j][i])
    
    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = " "

class exp_Paddle(Power_up):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.yspeed=1
        self.xspeed=0
    def wall_collision(self):
        if self.ycord >=37:
            global_var.render_E =1
    def paddle_collision(self):
        if self.ycord==35:
            # arr = [global_var.Paddle.xcord,global_var.Paddle.xcord+1,global_var.Paddle.xcord+2,global_var.Paddle.xcord+3,global_var.Paddle.xcord+4]
            for i in range(global_var.Paddle.width):
                value= global_var.Paddle.xcord+i
                if self.xcord == value:
                    global_var.render_E =1
                    global_var.expand_paddle_flag=1
                    global_var.expand_time_remain=round(time())+15
                    # global_var.Paddle.render()
                    # print(global_var.expand_paddle_flag)
    def render(self):
        if self.ycord + self.yspeed <=38:
            self.ycord+=self.yspeed
        if self.xcord + self.xspeed <=2 :
            self.xspeed*=-1
        if self.xcord + self.xspeed >=95:
            self.xspeed*=-1
        self.xcord+=self.xspeed
        self.paddle_collision()
        self.wall_collision()
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.GREEN+self.shape[j][i])
    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = " "

class shrink_Paddle(Power_up):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.yspeed=1
        self.xspeed=0
    def wall_collision(self):
        if self.ycord >=37:
            global_var.render_S =1
    def paddle_collision(self):
        if self.ycord==35:
            # arr = [global_var.Paddle.xcord,global_var.Paddle.xcord+1,global_var.Paddle.xcord+2,global_var.Paddle.xcord+3,global_var.Paddle.xcord+4]
            for i in range(global_var.Paddle.width):
                value= global_var.Paddle.xcord+i
                if self.xcord == value:
                    global_var.render_S =1
                    global_var.shrink_paddle_flag=1
                    global_var.shrink_time_remain=round(time())+15
                    # global_var.Paddle.render()
                    # print(global_var.expand_paddle_flag)
    def render(self):

        if self.ycord + self.yspeed <=38:
            self.ycord+=self.yspeed
        if self.xcord+ self.xspeed <=2 :
            self.xspeed*=-1
        if self.xcord+ self.xspeed >=95:
            self.xspeed*=-1
        self.xcord+=self.xspeed
        self.paddle_collision()
        self.wall_collision()
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.GREEN+self.shape[j][i])
    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = " "

class paddle_grab(Power_up):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.yspeed=1
        self.xspeed=0
    def wall_collision(self):
        if self.ycord >=37:
            global_var.render_P =1
    def paddle_collision(self):
        if self.ycord==35:
            # arr = [global_var.Paddle.xcord,global_var.Paddle.xcord+1,global_var.Paddle.xcord+2,global_var.Paddle.xcord+3,global_var.Paddle.xcord+4]
            for i in range(global_var.Paddle.width):
                value= global_var.Paddle.xcord+i
                if self.xcord == value:
                    global_var.render_P =1
                    global_var.paddle_grab_flag=1
                    global_var.paddle_time_remain=round(time())+15
                    # global_var.Paddle.render()
                    # print(global_var.expand_paddle_flag)
    def render(self):

        if self.ycord + self.yspeed <=38:
            self.ycord+=self.yspeed
        if self.xcord + self.xspeed <=2 :
            self.xspeed*=-1
        if self.xcord+ self.xspeed >=95:
            self.xspeed*=-1
        self.xcord+=self.xspeed
        self.paddle_collision()
        self.wall_collision()
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.GREEN+self.shape[j][i])
class Fast_ball(Power_up):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.yspeed=1
        self.xspeed=0
    def wall_collision(self):
        if self.ycord >=37:
            global_var.render_F =1
    def paddle_collision(self):
        if self.ycord==35:
            # arr = [global_var.Paddle.xcord,global_var.Paddle.xcord+1,global_var.Paddle.xcord+2,global_var.Paddle.xcord+3,global_var.Paddle.xcord+4]
            for i in range(global_var.Paddle.width):
                value= global_var.Paddle.xcord+i
                if self.xcord == value:
                    global_var.render_F =1
                    global_var.fast_ball_flag=1
                    if global_var.ball.xspeed < 0 :
                        global_var.ball.xspeed -=1
                    else:
                        global_var.ball.xspeed += 1
                    
                    # global_var.Paddle.render()
                    # print(global_var.expand_paddle_flag)
    def render(self):
        if self.ycord + self.yspeed <=38:
            self.ycord+=self.yspeed
        if self.xcord + self.xspeed<=2 :
            self.xspeed*=-1
        if self.xcord + self.xspeed>=95:
            self.xspeed*=-1
        self.xcord+=self.xspeed
        self.paddle_collision()
        self.wall_collision()
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.GREEN+self.shape[j][i])

class Fire_ball(Power_up):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.yspeed=1
        self.xspeed=0
    def wall_collision(self):
        # global_var.render_fb 
        if self.ycord >=37:
            global_var.render_fb =1
    def paddle_collision(self):
        if self.ycord==35:
            # arr = [global_var.Paddle.xcord,global_var.Paddle.xcord+1,global_var.Paddle.xcord+2,global_var.Paddle.xcord+3,global_var.Paddle.xcord+4]
            for i in range(global_var.Paddle.width):
                value= global_var.Paddle.xcord+i
                if self.xcord == value:
                    global_var.render_fb =1
                    global_var.fire_ball_flag=1
                    global_var.fire_ball_time_remain=round(time())+5
    # def inc_speed(self):
      
    def render(self):
        # self.inc_speed()
        if self.xcord + self.xspeed<=2 :
            self.xspeed*=-1
        if self.xcord + self.xspeed>=95:
            self.xspeed*=-1
        self.xcord+=self.xspeed        
        if self.ycord <=38:
            self.ycord+=self.yspeed
        # else:
        #     self.ycord = 38
        #     self.xcord = 95

        self.paddle_collision()
        self.wall_collision()

        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.GREEN+self.shape[j][i])
class Bullets(Power_up):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)
        self.yspeed=1
        self.xspeed=0
    def wall_collision(self):
        # global_var.render_fb 
        if self.ycord >=37:
            global_var.render_bullet =1
    def paddle_collision(self):
        if self.ycord==35:
            # arr = [global_var.Paddle.xcord,global_var.Paddle.xcord+1,global_var.Paddle.xcord+2,global_var.Paddle.xcord+3,global_var.Paddle.xcord+4]
            for i in range(global_var.Paddle.width):
                value= global_var.Paddle.xcord+i
                if self.xcord == value:
                    global_var.render_bullet =1
                    global_var.fire_bullet_flag=1
                    global_var.fire_bullet.xcord=global_var.Paddle.xcord
                    global_var.fire_bullet_time_remain=round(time())+10
    # def inc_speed(self):
      
    def render(self):
        # self.inc_speed()
        if self.ycord <=38:
            self.ycord+=self.yspeed
        if self.xcord+self.xspeed <=2 :
            self.xspeed*=-1
        if self.xcord +self.xspeed>=95:
            self.xspeed*=-1
        self.xcord+=self.xspeed
        self.paddle_collision()
        self.wall_collision()

        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = (Fore.GREEN+self.shape[j][i])                   

class UFO(Main):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)  
        self.lives=12
    
    def movement(self):
        self.xcord=global_var.Paddle.xcord
    # def collision(self):

    def render(self):
        self.movement()
        for i in range(self.width):
            for j in range(self.height):
                # print("Hi   ")
                global_var.mp.grid[j+self.ycord][i+self.xcord] = self.shape[j][i]

class shoot_bullet(Main):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)  
        self.yspeed=1
    # def collision(self):
    #     if self.ycord==35:
    #         for i in range(global_var.Paddle.width):
    #             value= global_var.Paddle.xcord+i
    #             if self.xcord == value:  
    #                 # global_var.score+=10000
    #                 global_var.lives = global_var.lives-1 
    #         self.ycord=global_var.Enemy.ycord
    #         self.xcord=global_var.Enemy.xcord
    #         # self.shape = [[' ']]       
    def render(self):
        if self.ycord+self.yspeed >=7:       
            self.ycord-=self.yspeed
        else :
            self.ycord=global_var.Paddle.ycord
            self.xcord=global_var.Paddle.xcord

        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = self.shape[j][i]    
class Bomb(Main):
    def __init__(self, feature,x, y):
        super().__init__(feature, x, y)  
        self.yspeed=1
    def collision(self):
        if self.ycord==35:
            for i in range(global_var.Paddle.width):
                value= global_var.Paddle.xcord+i
                if self.xcord == value:  
                    # global_var.score+=10000
                    global_var.lives = global_var.lives-1 
            self.ycord=global_var.Enemy.ycord
            self.xcord=global_var.Enemy.xcord
            # self.shape = [[' ']]       
    def render(self):
        self.collision()
        if self.ycord <=35:
            self.ycord+=self.yspeed
        val = round(time()) - global_var.time
        # if val%4 == 0 :
        #     self.xcord=global_var.Enemy.xcord
        #     self.ycord=global_var.Enemy.ycord
        #     self.shape=[[' ']]

        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.grid[j+self.ycord][i+self.xcord] = self.shape[j][i]    


def Deal_Exposion(x,y):
    global_var.arr.append((x-1,y))
    global_var.arr.append((x+1,y))
    global_var.arr.append((x,y+1))
    global_var.arr.append((x,y-1))
    global_var.arr.append((x+1,y+1))
    global_var.arr.append((x-1,y+1))
    global_var.arr.append((x-1,y-1))
    global_var.arr.append((x+1,y-1))

def fire_with_fire(x,y):
    global_var.fire_arr.append((x-1,y))
    global_var.fire_arr.append((x+1,y))
    global_var.fire_arr.append((x,y+1))
    global_var.fire_arr.append((x,y-1))
    global_var.fire_arr.append((x+1,y+1))
    global_var.fire_arr.append((x-1,y+1))
    global_var.fire_arr.append((x-1,y-1))
    global_var.fire_arr.append((x+1,y-1))    
   
def reset_flag():
    if round(time())==global_var.thru_time_remain:
        global_var.thru_ball_flag = 0
    if round(time()) == global_var.expand_time_remain:
        global_var.expand_paddle_flag =0
    if round(time())== global_var.shrink_time_remain:
        global_var.shrink_paddle_flag=0
    if round(time())==global_var.paddle_time_remain:    
        global_var.paddle_grab_flag=0
    if round(time())==global_var.fire_ball_time_remain:    
        global_var.fire_ball_flag=0
    if round(time())==global_var.fire_bullet_time_remain:    
        global_var.fire_bullet_flag=0
def make_bricks():

    brick1 = []
    for i in range(1,90):
        brick1.append(Brick_l1(config.brick,i,9))

    global_var.enemybricks.append(brick1)
    # global_var.Bricks.append(brick1)

def score_render():
    print("Score: ",global_var.score)
    print("Lives: ",global_var.lives)
    print("Time: ",round(time())-global_var.time)
    print("Level:",global_var.level)
    if round(time())-global_var.time==10 and global_var.level == 1:
        global_var.fall_brick_flag=1
    if (global_var.time2 + 10) == (round(time()) - global_var.time):
        global_var.fall_brick_flag =1
    if (global_var.time3 + 10 ) == (round(time()) - global_var.time):
        global_var.fall_brick_flag=1
    if global_var.fire_bullet_flag ==1:
        print("Time Left :  " ,global_var.fire_bullet_time_remain - round(time()))
    print()
    if global_var.level==3:
        if global_var.Enemy.lives == 10 and global_var.make_bricks_flag==0 :
            make_bricks()
            global_var.make_bricks_flag=1
        if global_var.Enemy.lives == 2 and global_var.make_bricks_flag2==0:
            make_bricks()
            global_var.make_bricks_flag2=1
        if global_var.Enemy.lives==0:
            global_var.game_over=1
        print("Health of UFO:",global_var.Enemy.lives)
def update_powerups():
    global_var.paddle_grab_flag_c=0

    global_var.expand_paddle_flag_c=0
    global_var.shrink_paddle_flag_c=0
    global_var.fire_ball_flag_c= 0

    global_var.thru_ball_flag_c=0
    global_var.fast_ball_flag_c=0


    global_var.T_ball.ycord = 14
    global_var.F_ball.ycord = 14
    global_var.E_paddle .ycord = 14
    global_var.S_paddle.ycord = 14
    global_var.P_grab.ycord = 14
    global_var.D_ball.ycord = 14


def update_level():
    if global_var.level == 4: 
        return 1
    global_var.Paddle.clear()
    global_var.thru_ball_flag=0
    global_var.expand_paddle_flag=0
    global_var.shrink_paddle_flag=0
    global_var.paddle_grab_flag=0
    global_var.fast_ball_flag=0
    global_var.fire_ball_flag=0
    global_var.fall_brick_flag=0

    global_var.Paddle = paddle(config.paddle, 50, 35, global_var.lives)
    # global_var.lives=1
    # global_var.ball.clear()
    global_var.time2 = round(time())  -global_var.time
    global_var.ball = Ball(config.ball,52,34)
    global_var.T_ball.xcord=12
    global_var.E_paddle.xcord=24
    global_var.S_paddle.xcord=36
    global_var.F_ball.xcord=18
    global_var.D_ball.xcord=20
    global_var.P_grab.xcord=16
    global_var.bullet.xcord=40
    global_var.ball.xspeed =0 
    global_var.ball.yspeed = 0
    global_var.default = 0
    for i in global_var.Bricks:
        for j in i:
            j.clear()
    # for i in  global_var.brick1:
    #     i.clear()
    # for i in  global_var.brick2:
    #     i.clear()
    # for i in  global_var.brick3:
    #     i.clear()
    # for i in  global_var.brick4:
    #     i.clear()
    # for i in  global_var.brick5:
    #     i.clear()
    global_var.Bricks = []
    global_var.brick1  = []
    global_var.brick2  = []
    global_var.brick3  = []
    global_var.brick4  = []
    global_var.brick5  = []
    if global_var.level == 3:
        global_var.time3 = round(time())  -global_var.time
        global_var.Bricks=global_var.make_level3_bricks()
        return 0
    elif global_var.level ==2 :
        global_var.time2 = round(time())  -global_var.time
        global_var.Bricks = global_var.make_level2_bricks()
        update_powerups()
        return 0


# def deploy_bomb():
#     if global_var.level==3:
#         bomb= Bomb(config.Bomb,)