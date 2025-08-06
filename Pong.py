# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
global paddle1_1_n, paddle1_2_n
paddle1_1_n = 175
paddle1_2_n = 225
paddle2_1_n = 175
paddle2_2_n = 225
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [300, 200]
ball_vel = [0,0]
paddle1_pos = [(0, paddle1_1_n), (0, paddle1_2_n), (8, paddle1_2_n), (8, paddle1_1_n)] 
paddle2_pos = [(600, paddle2_1_n), (600, paddle2_2_n), (592, paddle2_2_n), (592, paddle2_1_n)]
paddle1_vel = [0,0]
paddle2_vel = [0,0]
t = True
a = True
b = True
c = True
d = True
score2 = 0
score1 = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300, 200]
    if direction == RIGHT:
        #ball_pos = [300, 200]
        ball_vel = [(random.randrange(150, 270)/ 100.0), -(random.randrange(100, 220)/ 100.0)]
    elif direction == LEFT:
        #ball_pos = [300, 200]
        ball_vel = [-(random.randrange(150, 270)/ 100.0), -(random.randrange(100, 220)/ 100.0)]
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, paddle1_1_n, paddle2_2_n, paddle1_2_n, paddle2_1_n  # these are numbers
    global score1, score2, t  # these are ints
    #if t == True:
        #t = False
    paddle1_1_n = 175
    paddle1_2_n = 225
    paddle2_1_n = 175
    paddle2_2_n = 225
    spawn_ball(random.choice((RIGHT, LEFT)))
    paddle2_pos = [(600, paddle2_1_n), (600, paddle2_2_n), (592, paddle2_2_n), (592, paddle2_1_n)]
    paddle1_pos = [(0, paddle1_1_n), (0, paddle1_2_n), (8, paddle1_2_n), (8, paddle1_1_n)] 
    score1 = 0
    score2 = 0
    #if ball_pos[1] <= BALL_RADIUS:
        #ball_vel[1] = -ball_vel[1]
    #elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        #ball_vel[1] = -ball_vel[1]
        
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_1_n, paddle1_2_n,paddle2_1_n, paddle2_2_n
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] > paddle1_1_n - 15 -2 and ball_pos[1]<paddle1_2_n + 15 +2 and ball_pos[0] - BALL_RADIUS <= PAD_WIDTH+2:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] > paddle2_1_n - 15 -2 and ball_pos[1] < paddle2_1_n + 15 +2 and WIDTH - (WIDTH - (ball_pos[0] + BALL_RADIUS)) >= (WIDTH - PAD_WIDTH) -2:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:        
        ball_vel = [0,0]
        spawn_ball(RIGHT)
        score2 += 1
    elif ball_pos[0] >= WIDTH - PAD_WIDTH-BALL_RADIUS:
        #ball_pos = [300, 200]
        ball_vel = [0,0]
        spawn_ball(LEFT)
        score1 += 1
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # draw mid line and gutters
    canvas.draw_circle((ball_pos), 20, 1, "White", "White")
    canvas.draw_polygon((paddle2_pos), 1, "White", "White")
    # update ball
    #ball_pos[1] += ball_vel[1]       
    # draw ball
    #ball_pos[0] += ball_vel[0]
    # update paddle's vertical position, keep paddle on the screen
    #paddle1_vertical = [paddle1_pos[0],paddle1_pos[1], paddle1_pos[2], paddle1_pos[3]]
    paddle1_1_n += paddle1_vel[1]
    paddle1_2_n += paddle1_vel[1]
    paddle2_1_n += paddle2_vel[1]
    paddle2_2_n += paddle2_vel[1]
    paddle1_pos = [(0, paddle1_1_n), (0, paddle1_2_n), (8, paddle1_2_n), (8, paddle1_1_n)] 
    paddle2_pos = [(600, paddle2_1_n), (600, paddle2_2_n), (592, paddle2_2_n), (592, paddle2_1_n)]
    canvas.draw_polygon((paddle1_pos), 1, "White", "White")
    # draw paddles
    canvas.draw_polygon((paddle2_pos), 1, "White", "White")
    # determine whether paddle and ball collide    
    if paddle1_1_n <= 0:
        paddle1_vel[1] = 0
        global a
        a = False
    if paddle1_2_n >= 400:
        paddle1_vel[1] = 0
        global d
        d = False
    if paddle2_1_n <= 0:
        global c
        c = False
        paddle2_vel[1] = 0
        #global b
        #b = False
    if paddle2_2_n >= 400:
        paddle2_vel[1] = 0
        global b
        b = False
    # draw scores
    canvas.draw_text(str(score1),[125, 30], 40, "Blue")
    canvas.draw_text(str(score2), [425, 30], 40, "Green")
def keydown(key):
    global paddle1_vel, paddle2_vel, a, b, c, d
    if b == True and key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 4
        c = True
    if c == True and key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -4
        b = True
    if a == True and key == simplegui.KEY_MAP["W"]:
        paddle1_vel[1] = -4
        d = True
    if d == True and key == simplegui.KEY_MAP["S"]:
        paddle1_vel[1] = 4
        a = True

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    if key == simplegui.KEY_MAP["W"]:
        paddle1_vel[1] = 0
    if key == simplegui.KEY_MAP["S"]:
        paddle1_vel[1] = 0
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


# start frame
new_game()
frame.start()
