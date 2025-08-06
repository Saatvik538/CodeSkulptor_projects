# implementation of card game - Memory

import simplegui
import random
turn = 0

# helper function to initialize globals
def new_game():
    global Cards, state, exposed, e, click, turn, card_list
    card_list = []
    Cards = list(range(0,8))
    x = list(range(0,8))
    Cards += x
    random.shuffle(Cards)
    #exposed = False
    e = 0
    turn = 0
    #click = [0, 0]
    exposed =[False for c in range(16)]
    #print Cards, exposed
    

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    
    global e, exposed, click, turn, card_list
    click = pos[0]//50
    if e == 0:
        e = 1
        card_list.append(click)
        turn +=1
        exposed[click] = True
        #a = Cards[click]
        #c = click
    elif e == 1:
        if not (click in card_list) and exposed[click] == False:
            card_list.append(click)
            turn += 1
            exposed[click] = True
            e = 2
            #b = Cards[click]
            #d = click
    else:
        if exposed[click] == False and Cards[card_list[-1]] != Cards[card_list[-2]]:
            turn += 1
            exposed[card_list[-1]] = False
            exposed[card_list[-2]] = False
            exposed[click] = True
            e = 1
            card_list.pop()
            card_list.pop()
            card_list.append(click)
        elif Cards[card_list[-1]] == Cards[card_list[-2]]:
            e = 1
            exposed[click] = True
            card_list.append(click)
    
                        
# cards are logically 50x100 pixels in size 
def draw(canvas):
    label.set_text("Turns = "+str(turn))
    Card_pos = 0
    #n = 0
    global exposed, click
    for n in range(len(Cards)):
        Card_pos = 50 * n
        #if e == 1 or 0 and n == 0:
        if exposed[n] == True:
            #if click[0] - 10 <= Card_pos[0] or click[0] + 10 <= Card_pos[0] : 
            #n = 1
            canvas.draw_text(str(Cards[n]), [Card_pos+15, 60], 40, "Blue")
        else:
            canvas.draw_polygon([(Card_pos,0), (Card_pos, 100), (Card_pos + 50, 100), (Card_pos +50, 0)], 1, "Red", "Green")
        #if e == 2 and n == 0:
        if exposed[n] == True:
            #if click[0] - 10 <= Card_pos[0]: 
            #n = 1
            canvas.draw_text(str(Cards[n]), [Card_pos+15,60], 40, "Blue")
        #canvas.draw_line((50,120), (50, 0), 1, "White")
        #canvas.draw_line((100,120), (100, 0), 1, "White")
        #canvas.draw_line((145,120), (145, 0), 1, "White")
        #canvas.draw_line((195,120), (195, 0), 1, "White")
        #canvas.draw_line((200,120), (200, 0), 1, "White")
        #canvas.draw_line((250,120), (250, 0), 1, "White")
        #canvas.draw_line((300,120), (300, 0), 1, "White")
        #canvas.draw_line((345,120), (345, 0), 1, "White")
        #canvas.draw_line((400,120), (400, 0), 1, "White")
        #canvas.draw_line((450,120), (450, 0), 1, "White")
        #canvas.draw_line((495,120), (495, 0), 1, "White")
        #canvas.draw_line((545,120), (545, 0), 1, "White")
        #canvas.draw_line((600,120), (600, 0), 1, "White")
        #canvas.draw_line((650,120), (650, 0), 1, "White")
        #canvas.draw_line((700,120), (700, 0), 1, "White")
        #canvas.draw_line((750,120), (750, 0), 1, "White")
        #canvas.draw_line((780,120), (780, 0), 1, "White")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turn))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric