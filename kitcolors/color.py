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

    def __post_init__(self) -> None:
        _RED, _GREEN, _BLUE = self.RGB
        if not (0 <= _RED <= 255 and 0 <= _GREEN <= 255 and 0 <= _BLUE <= 255):
            raise ColorValueError(
                "RGB values must be in the range [0, 255], "
                f"but are ({_RED},{_GREEN},{_BLUE})"
            )

        self.rgb = (_RED / 255, _GREEN / 255, _BLUE / 255)
        self.hex = f"#{int(_RED):02X}{int(_GREEN):02X}{int(_BLUE):02X}"

    @staticmethod
    def _validate_alpha(alpha: float) -> None:
        if not 0 <= alpha <= 1:
            raise AlphaValueError(
                f"Alpha value must be in the range [0, 1], but is {alpha}"
            )

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
