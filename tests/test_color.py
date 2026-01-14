import pytest
from kitcolors import Color
from kitcolors.color import AlphaValueError, ColorValueError


class TestHex:
    def test_black(self):
        assert Color("black", (0, 0, 0)).hex == "#000000"

    def test_white(self):
        assert Color("white", (255, 255, 255)).hex == "#FFFFFF"

    def test_red(self):
        assert Color("red", (255, 0, 0)).hex == "#FF0000"

    def test_green(self):
        assert Color("green", (0, 255, 0)).hex == "#00FF00"

    def test_blue(self):
        assert Color("blue", (0, 0, 255)).hex == "#0000FF"

    def test_kit_green(self):
        assert Color("kit_green", (0, 150, 130)).hex == "#009682"


class TestHexa:
    def test_fully_opaque(self):
        color = Color("red", (255, 0, 0))
        assert color.hexa(1.0) == "#FF0000FF"

    def test_fully_transparent(self):
        color = Color("red", (255, 0, 0))
        assert color.hexa(0.0) == "#FF000000"

    def test_half_transparent(self):
        color = Color("white", (255, 255, 255))
        # 0.5 * 255 = 127.5 -> int = 127 -> 7F
        assert color.hexa(0.5) == "#FFFFFF7F"


class TestRgbProperty:
    def test_black(self):
        color = Color("black", (0, 0, 0))
        assert color.rgb == (0.0, 0.0, 0.0)

    def test_white(self):
        color = Color("white", (255, 255, 255))
        assert color.rgb == (1.0, 1.0, 1.0)

    def test_mid_gray(self):
        color = Color("gray", (128, 128, 128))
        expected = 128 / 255
        assert color.rgb == (expected, expected, expected)


class TestValidation:
    @pytest.mark.parametrize("invalid_rgb", [
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
        (256, 0, 0),
        (0, 256, 0),
        (0, 0, 256),
    ])
    def test_invalid_rgb_raises(self, invalid_rgb):
        with pytest.raises(ColorValueError):
            Color("invalid", invalid_rgb)

    @pytest.mark.parametrize("valid_rgb", [
        (0, 0, 0),
        (255, 255, 255),
        (0, 255, 0),
    ])
    def test_valid_rgb_boundary(self, valid_rgb):
        color = Color("valid", valid_rgb)
        assert color.RGB == valid_rgb

    @pytest.mark.parametrize("invalid_alpha", [-0.1, 1.1, -1, 2])
    def test_invalid_alpha_rgba(self, invalid_alpha):
        color = Color("test", (100, 100, 100))
        with pytest.raises(AlphaValueError):
            color.rgba(invalid_alpha)

    @pytest.mark.parametrize("invalid_alpha", [-0.1, 1.1, -1, 2])
    def test_invalid_alpha_RGBa(self, invalid_alpha):
        color = Color("test", (100, 100, 100))
        with pytest.raises(AlphaValueError):
            color.RGBa(invalid_alpha)

    @pytest.mark.parametrize("invalid_alpha", [-0.1, 1.1, -1, 2])
    def test_invalid_alpha_hexa(self, invalid_alpha):
        color = Color("test", (100, 100, 100))
        with pytest.raises(AlphaValueError):
            color.hexa(invalid_alpha)

    @pytest.mark.parametrize("valid_alpha", [0.0, 0.5, 1.0])
    def test_valid_alpha_boundary(self, valid_alpha):
        color = Color("test", (100, 100, 100))
        color.rgba(valid_alpha)
        color.RGBa(valid_alpha)
        color.hexa(valid_alpha)
