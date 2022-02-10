pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let is_pin1 = input.pinIsPressed(TouchPin.P1)
let is_pin2 = input.pinIsPressed(TouchPin.P2)
let start = false
let not_pressed = true
let player1 = false
let player2 = false
let Tie = false
let jenoha = true
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    player1 = true
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    player2 = true
})
basic.forever(function on_forever() {
    console.logValue("x", player1)
    
    basic.pause(randint(3000, 10000))
    start = true
    basic.showIcon(IconNames.Heart)
    music.playTone(Note.C, 1000)
    while (jenoha == true) {
        
    }
})
control.inBackground(function run_parallel() {
    if (player1 == true && start == true) {
        basic.showNumber(1)
        basic.pause(3000)
        control.reset()
    } else if (player2 == true && start == true) {
        basic.showNumber(2)
        basic.pause(3000)
        control.reset()
    } else if (player1 == true && player2 && start == true) {
        basic.showString("R")
        basic.pause(3000)
        control.reset()
    } else if (player1 == true && start == false) {
        basic.showString("B")
        basic.pause(3000)
        control.reset()
    } else if (player2 == true && start == false) {
        basic.showString("A")
        basic.pause(3000)
        control.reset()
    }
    
})
