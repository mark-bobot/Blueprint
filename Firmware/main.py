import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros, Press, Release, Tap, Delay

keyboard = KMKKeyboard()

keyboard.matrix = KeysScanner(
    pins=(board.D4, board.D6, board.D7, board.D5, board.D3),
    value_when_pressed=False,
)

encoder = EncoderHandler()
encoder.pins = ((board.D1, board.D2, None, False),)
keyboard.modules.append(encoder)

macros = Macros()
keyboard.modules.append(macros)

OPEN_CLAUDE = KC.MACRO(
    Press(KC.LGUI), Tap(KC.T), Release(KC.LGUI),
    Delay(300),
    "claude.ai",
    Tap(KC.ENTER),
)

keyboard.keymap = [
    [
        KC.LGUI(KC.C),
        KC.LGUI(KC.V),
        KC.LGUI(KC.LSFT(KC.M)),
        OPEN_CLAUDE,
        KC.MUTE,
    ],
]

encoder.map = [
    ((KC.VOLD, KC.VOLU),),
]

if __name__ == "__main__":
    keyboard.go()
