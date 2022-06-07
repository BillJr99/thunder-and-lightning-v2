def on_sound_loud():
    global sound_time, time_delta, light_time
    if light_time > 0 and sound_time == 0:
        basic.show_icon(IconNames.YES)
        sound_time = control.millis()
        time_delta = sound_time - light_time
        time_delta = time_delta / 1000
        time_delta = time_delta / 5
        basic.show_number(time_delta)
        light_time = 0
input.on_sound(DetectedSound.LOUD, on_sound_loud)

current_light = 0
time_delta = 0
light_time = 0
sound_time = 0
sound_time = 0
light_time = 0
time_delta = 0

def on_forever():
    global current_light, light_time
    current_light = input.light_level()
    if current_light > 140 and light_time == 0:
        basic.show_icon(IconNames.CHESSBOARD)
        light_time = control.millis()
basic.forever(on_forever)
