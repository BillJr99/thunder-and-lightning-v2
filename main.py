def on_sound_loud():
    if light_time > 0 and sound_time == 0:
        sound_time = control.millis()
        light_time = 0
        
input.on_sound(DetectedSound.LOUD, on_sound_loud)

light_time = 0
sound_time2 = 0

def on_forever():
    global light_time
    current_light = 0
    if current_light > 80 and light_time == 0:
        light_time = control.millis()
basic.forever(on_forever)
