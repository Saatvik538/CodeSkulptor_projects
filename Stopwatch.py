# template for "Stopwatch: The Game"
import simplegui
import collections
# define global variables
tenth = 0.0
ten = 0
minute = 0
x = 0
y = 0
h = True
def tick():
    global tenth, ten, minute
    if tenth - 9.8 >= 0.0:
        tenth = 0.0
        ten += 1
    elif ten - 6 >= 0:
        ten = 0
        minute += 1
    tenth += 0.1
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
#def form(t):
    
    #global tenth, ten
    #if tenth == 10.0:
        #tenth = 0.0
        #ten = 1
    #elif ten == 6:
        #ten = 0
        #minute = 1
    #t = str(minute) + ":" + str(ten) + str(tenth) 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global h
    h = True
def stop():
    global h
    if h == True:
        timer.stop()
        global tenth, y
        global x, t
        x += 1
        t = (str(tenth)[2])
        h = False
        if int(t) == 0:
            y += 1
def reset():
    global tenth,ten,minute, y ,x
    ten = 0
    minute = 0
    tenth = 0.0
    y = 0
    x = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
#def tick():
    #global tenth
    #tenth += 0.1
# define draw handler
def draw(canvas):
    canvas.draw_text(str(minute) + ":" + str(ten) + str(tenth) , [100, 100], 50, "White")
    canvas.draw_text( str(x) + "/" + str(y), [250, 20], 30, 'Green')
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
# register event handlers
frame.add_button("Reset", reset)
frame.add_button("Start", start)
frame.add_button("Stop", stop)

# start frame
frame.start()

# Please remember to review the grading rubric
