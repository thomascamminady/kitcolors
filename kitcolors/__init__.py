from kitcolors.color import Color

__version__ = "1.8.0"
__all__ = [
    "Color",
    "white",
    "black",
    "green",
    "blue",
    "maygreen",
    "yellow",
    "orange",
    "brown",
    "red",
    "purple",
    "cyan",
    "kitcolors",
]

white = Color("white", (255, 255, 255))
black = Color("black", (0, 0, 0))
green = Color("green", (0, 150, 130))
blue = Color("blue", (70, 100, 170))
maygreen = Color("maygreen", (140, 182, 60))
yellow = Color("yellow", (252, 229, 0))
orange = Color("orange", (223, 155, 27))
brown = Color("brown", (167, 130, 46))
red = Color("red", (162, 34, 35))
purple = Color("purple", (163, 16, 124))
cyan = Color("cyan", (35, 161, 224))


kitcolors = {
    "white": white,
    "black": black,
    "green": green,
    "blue": blue,
    "maygreen": maygreen,
    "yellow": yellow,
    "orange": orange,
    "brown": brown,
    "red": red,
    "purple": purple,
    "cyan": cyan,
}
