from collections import namedtuple

Sound = namedtuple("Sound", ["note", "freq", "altsax"])
SOUND_LIST = [
    Sound("B3", 246.94, "ソ#3"),  # ピアノのシ
    Sound("C4", 261.63, "ラ4"),  # ピアノのド
    Sound("C#4", 277.18, "シ♭4"),  # ピアノのド#
    Sound("D4", 293.66, "シ4"),  # ピアノのレ
    Sound("E4", 329.63, "ド#4"),  # ピアノのミ
    Sound("F4", 349.23, "レ4"),  # ピアノのファ
    Sound("G4", 392, "ミ"),  # ピアノのソ
    Sound("A4", 440, "ファ#4"),  # ピアノのラ
    Sound("B4", 493.88, "ソ#4"),  # ピアノのシ
    Sound("C4", 523.25, "ラ4"),  # ピアノのド
    Sound("D4", 587.33, "シ4"),  # ピアノのレ
    Sound("E4", 659.25, "ド#4"),  # ピアノのミ
    Sound("F4", 698.46, "レ4"),  # ピアノのファ
    Sound("G4", 783.99, "ミ4"),  # ピアノのソ
]
# TODO: 曲によっては追加が必要
