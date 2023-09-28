import kitcolors
import pytest


@pytest.mark.parametrize("alpha", [0.0, 0.1, 0.5, 0.9, 1.0])
@pytest.mark.parametrize("color", kitcolors.kitcolors.values())
def test_equivalence_transparent_nontransparent_rgb(
    color: kitcolors.Color, alpha: float
):
    rgba = color.rgba(alpha, transparent=True)
    rgb = color.rgba(alpha, transparent=False)

    for i in range(3):
        assert rgba[i] * rgba[-1] + 1 * (1 - rgba[-1]) == rgb[i]


@pytest.mark.parametrize("alpha", [0.0, 0.1, 0.5, 0.9, 1.0])
@pytest.mark.parametrize("color", kitcolors.kitcolors.values())
def test_equivalence_transparent_nontransparent_RGB(
    color: kitcolors.Color, alpha: float
):
    RGBa = color.RGBa(alpha, transparent=True)
    RGB = color.RGBa(alpha, transparent=False)

    for i in range(3):
        assert RGBa[i] * RGBa[-1] + 255 * (1 - RGBa[-1]) == RGB[i]


@pytest.mark.parametrize(
    "name,color",
    [
        ("white", kitcolors.white),
        ("black", kitcolors.black),
        ("green", kitcolors.green),
        ("blue", kitcolors.blue),
        ("maygreen", kitcolors.maygreen),
        ("yellow", kitcolors.yellow),
        ("orange", kitcolors.orange),
        ("brown", kitcolors.brown),
        ("red", kitcolors.red),
        ("purple", kitcolors.purple),
        ("cyan", kitcolors.cyan),
    ],
)
def test_name_is_consistent(name: str, color: kitcolors.Color):
    assert name == color.name
