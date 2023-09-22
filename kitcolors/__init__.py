from dataclasses import dataclass


@dataclass
class Color:
    """RGB values of the KIT color scheme."""

    name: str
    _RGB: tuple[int, int, int]

    @property
    def RGB(self) -> tuple[int, int, int]:
        """RGB values of this color, each in the range [0,255]."""
        return self._RGB

    @property
    def rgb(self) -> tuple[float, float, float]:
        """RGB values of this color, each in the range [0,1]."""
        _red, _green, _blue = self.RGB
        return (_red / 255, _green / 255, _blue / 255)

    @property
    def hex(self) -> str:
        """Hex value of the color."""
        _red, _green, _blue = self.RGB
        return f"#{int(_red):02X}{int(_green):02X}{int(_blue):02X}"

    def RGBa(self, alpha: float) -> tuple[float, float, float, float]:
        """RGB values of this color (in the range [0,255]) and alpha value."""

        return (*self.RGB, alpha)

    def rgba(self, alpha: float) -> tuple[float, float, float, float]:
        """RGB values of this color (in the range [0,1]) and alpha value."""
        return (*self.rgb, alpha)

    def hexa(self, alpha: float) -> str:
        """Hex value of the color, including alpha."""
        return f"{self.hex}{int(alpha * 255):02X}"


white = Color("white", (255, 255, 255))
black = Color("black", (0, 0, 0))
green = Color("green", (0, 150, 130))
blue = Color("blue", (70, 100, 170))
maygreen = Color("maygren", (140, 182, 60))
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
