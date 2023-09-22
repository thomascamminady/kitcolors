from dataclasses import dataclass, field


class ColorValueError(ValueError):
    pass


class AlphaValueError(ValueError):
    pass


@dataclass
class Color:
    """Simple color class."""

    name: str
    RGB: tuple[int, int, int]
    rgb: tuple[float, float, float] = field(init=False)
    hex: str = field(init=False)

    @staticmethod
    def _validate_alpha(alpha: float) -> None:
        if not 0 <= alpha <= 1:
            raise AlphaValueError(
                f"Alpha value must be in the range [0, 1], but is {alpha}"
            )

    @staticmethod
    def _validate_rgb(red: int, green: int, blue: int) -> None:
        if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
            raise ColorValueError(
                "RGB values must be in the range [0, 255], "
                f"but are ({red},{green},{blue})"
            )

    def __post_init__(self) -> None:
        red, green, blue = self.RGB
        self._validate_rgb(red, green, blue)
        self.rgb = (red / 255, green / 255, blue / 255)
        self.hex = f"#{int(red):02X}{int(green):02X}{int(blue):02X}"

    def RGBa(self, alpha: float) -> tuple[int, int, int, float]:
        """RGB values of this color (in the range [0,255]) and alpha value."""
        self._validate_alpha(alpha)
        return (*self.RGB, alpha)

    def rgba(self, alpha: float) -> tuple[float, float, float, float]:
        """RGB values of this color (in the range [0,1]) and alpha value."""
        self._validate_alpha(alpha)
        return (*self.rgb, alpha)

    def hexa(self, alpha: float) -> str:
        """Hex value of the color, including alpha."""
        self._validate_alpha(alpha)
        return f"{self.hex}{int(alpha * 255):02X}"
