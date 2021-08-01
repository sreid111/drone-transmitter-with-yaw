pitch = 0
arm = 0
roll = 0
throttle = 0
yaw = 0
radio_group = 7
radio.set_group(radio_group)
basic.show_number(radio_group) 

def on_button_pressed_a():
    global throttle
    throttle -= 5
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global throttle
    throttle += 5
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    global arm
    global throttle
    throttle = 0
    if arm == 0:
        arm = 1
    else: 
        arm = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    global arm
    arm = 0
input.on_gesture(Gesture.Shake, on_gesture_shake)


def on_forever():
    #basic.show_number(arm)
    pitch = input.rotation(Rotation.PITCH)
    roll = input.rotation(Rotation.ROLL)
    basic.clear_screen()
    if arm == 1:
        led.plot(0, 0)
    led.plot(0, Math.map(throttle, 0, 100, 4, 0))
    led.plot(Math.map(roll, -45, 45, 0, 4), Math.map(pitch, -45, 45, 0, 4))
    radio.send_value("P", pitch)
    radio.send_value("A", arm)
    radio.send_value("R", roll)
    radio.send_value("T", throttle)
    radio.send_value("Y", yaw)
    

basic.forever(on_forever)
