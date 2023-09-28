from dataclasses import dataclass, field
from typing import overload, Literal


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

    @overload
    def RGBa(
        self, alpha: float, transparent: Literal[False]
    ) -> tuple[float, float, float]:
        ...

    @overload
    def RGBa(
        self, alpha: float, transparent: Literal[True]
    ) -> tuple[int, int, int, float]:
        ...

    def RGBa(
        self, alpha: float, transparent: bool = True
    ) -> tuple[float, float, float] | tuple[int, int, int, float]:
        """RGB values of this color (in the range [0,255]) and alpha value."""
        self._validate_alpha(alpha)

        if transparent:
            return (*self.RGB, alpha)
        else:
            red, green, blue, white = (*self.RGB, 255)

            def interpolate(color: int) -> float:
                return alpha * color + (1 - alpha) * white

            return (interpolate(red), interpolate(green), interpolate(blue))

    @overload
    def rgba(
        self, alpha: float, transparent: Literal[False]
    ) -> tuple[float, float, float]:
        ...

    @overload
    def rgba(
        self, alpha: float, transparent: Literal[True]
    ) -> tuple[float, float, float, float]:
        ...

    def rgba(
        self, alpha: float, transparent: bool = True
    ) -> tuple[float, float, float] | tuple[float, float, float, float]:
        """RGB values of this color (in the range [0,1]) and alpha value."""
        self._validate_alpha(alpha)
        if transparent:
            return (*self.rgb, alpha)
        else:
            red, green, blue, white = (*self.rgb, 1.0)

            def interpolate(color: float) -> float:
                return alpha * color + (1 - alpha) * white

            return (interpolate(red), interpolate(green), interpolate(blue))

    def hexa(self, alpha: float) -> str:
        """Hex value of the color, including alpha."""
        self._validate_alpha(alpha)
        return f"{self.hex}{int(alpha * 255):02X}"
