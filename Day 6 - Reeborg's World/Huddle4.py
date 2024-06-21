# logoReeborg's World

# Hurdle 4 ✓🤖
#  World Info 
# Python
#  Reeborg's keyboard Additional options
# English
 

# reverse step run step pause stop reload 
#  163/163   
# Python CodelibraryA↑AA↓A
()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right() 
    while front_is_clear():
        move()
    turn_left()        
   
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
