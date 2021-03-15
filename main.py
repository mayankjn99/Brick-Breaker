from input import *
import global_var
import board
import os 
import time
import objects

def cursor_hide():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

if __name__ == "__main__":
    take_input = Get()
    r = 0
    while 1:
        cursor_hide()
        if r == 1 : 
            # print("WIn")
            break
        if global_var.game_over == 1:
            break
        if global_var.score==50:
            global_var.level +=1
            r = objects.update_level()
        if global_var.score==80:
            global_var.level +=1
            r = objects.update_level()
        if global_var.score==150:
            global_var.level +=1
            r = objects.update_level()
        global_var.Paddle.clear()
        global_var.ball.clear()
        global_var.T_ball.clear()
        global_var.E_paddle.clear()
        global_var.S_paddle.clear()
        global_var.P_grab.clear()
        global_var.F_ball.clear()
        global_var.D_ball.clear()
        global_var.bullet.clear()
        if global_var.lives==0 :
            break
        val=input_to(take_input)
       
        if val != None:
            time.sleep(0.05)
        sys.stdout.write("\033c")
        
        if val == "a" : 
            global_var.Paddle.moveleft(-global_var.xspeed_paddle)
            if global_var.default == 0 :    
                global_var.ball.moveleftball(-global_var.xspeed_paddle)
            # global_var.ball.set_speed()

        elif val == "d" : 
            global_var.Paddle.moveright(global_var.xspeed_paddle)
            if global_var.default == 0 :   
                global_var.ball.moverightball(global_var.xspeed_paddle)
            
        if val == "r":
            global_var.default =1
            global_var.ball.set_speed()    
        # sys.stdout.flush()
        if val == "u":
            global_var.level +=1
            r = objects.update_level()
            # if r == 1:
            #     break
        if val == "q" :
            # print(val)
            break

            # global_var.clear_Tball=1
        
        global_var.Paddle.render()
        global_var.ball.render()
        global_var.ball.render_collision()
        if global_var.render_E ==0:
            global_var.E_paddle.render()
        if global_var.render_T == 0:
            global_var.T_ball.render()
        if global_var.render_S==0:
            global_var.S_paddle.render()
        if global_var.render_P == 0: 
            global_var.P_grab.render()
        if global_var.render_F==0:
            global_var.F_ball.render()
        if global_var.render_fb == 0:
            global_var.D_ball.render()
        if global_var.render_bullet ==0 :
            global_var.bullet.render()
        objects.reset_flag()
        global_var.mp.print_board()
        # global_var.find_time()
        sys.stdin.flush()
        objects.score_render()
        # global_var.brick.render()