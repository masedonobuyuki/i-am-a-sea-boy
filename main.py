

def on_button_pressed_a():
    basic.show_icon(IconNames.EIGTH_NOTE)
    muscicOnce()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . # # # #
                . # . . #
                . # . . #
                # # . # #
                # # . # #
    """)
    for index in range(4):
        muscicOnce()
        basic.pause(2000)
input.on_button_pressed(Button.B, on_button_pressed_b)

def muscicOnce():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.HALF))
basic.show_icon(IconNames.HEART)
music.set_volume(255)
music.set_tempo(84)