import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 60
g = "Green"
r = "red"
h = "DvD"
ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0 / 60.0,  5.0 / 60.0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
        global g, r, h
        g = "Red"
        r = "Green"
        h = "dVd"
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, g, r)
    canvas.draw_text(h, ball_pos, 30, "Blue")
# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
