input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.EigthNote)
    muscicOnce()
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . # # # #
        . # . . #
        . # . . #
        # # . # #
        # # . # #
        `)
    for (let index = 0; index < 4; index++) {
        muscicOnce()
        basic.pause(2000)
    }
})
function muscicOnce () {
    music.playTone(262, music.beat(BeatFraction.Whole))
    music.playTone(262, music.beat(BeatFraction.Whole))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(247, music.beat(BeatFraction.Half))
}
basic.showIcon(IconNames.Heart)
music.setVolume(255)
music.setTempo(84)
