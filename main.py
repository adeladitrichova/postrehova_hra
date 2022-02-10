pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)

is_pin1 = input.pin_is_pressed(TouchPin.P1)
is_pin2 = input.pin_is_pressed(TouchPin.P2)

start = False
not_pressed = True
player1 = False
player2 = False
Tie = False
jenoha = True

def on_forever():
    console.log_value("x", player1)
    global start, player1, player2, Tie
    basic.pause(randint(3000, 10000))
    start = True
    basic.show_icon(IconNames.HEART)
    music.play_tone(Note.C, 1000)
    while jenoha == True:
        pass

def on_pin_pressed_p1():
    global player1
    player1 = True
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_pin_pressed_p2():
    global player2
    player2 = True
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

basic.forever(on_forever)

def run_parallel():
    if player1 == True and start == True: 
        basic.show_number(1)
        basic.pause(3000)
        control.reset()

    elif player2 == True and start == True: 
        basic.show_number(2)
        basic.pause(3000)
        control.reset()

    elif player1 == True and player2 and start == True:
        basic.show_string("R")
        basic.pause(3000)
        control.reset()

    elif player1 == True and start == False:
        basic.show_string("B")
        basic.pause(3000)
        control.reset()

    elif player2 == True and start == False:
        basic.show_string("A")
        basic.pause(3000)
        control.reset()
control.in_background(run_parallel)