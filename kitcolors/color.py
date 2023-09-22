from dataclasses import dataclass, field


@dataclass
class Color:
    """RGB values of the KIT color scheme."""

    name: str
    RGB: tuple[int, int, int]
    rgb: tuple[float, float, float] = field(init=False)
    hex: str = field(init=False)

    def __post_init__(self):
        _red, _green, _blue = self.RGB
        self.rgb = (_red / 255, _green / 255, _blue / 255)
        self.hex = f"#{int(_red):02X}{int(_green):02X}{int(_blue):02X}"

    def RGBa(self, alpha: float) -> tuple[float, float, float, float]:
        """RGB values of this color (in the range [0,255]) and alpha value."""
        return (*self.RGB, alpha)

    def rgba(self, alpha: float) -> tuple[float, float, float, float]:
        """RGB values of this color (in the range [0,1]) and alpha value."""
        return (*self.rgb, alpha)

    def hexa(self, alpha: float) -> str:
        """Hex value of the color, including alpha."""
        return f"{self.hex}{int(alpha * 255):02X}"
