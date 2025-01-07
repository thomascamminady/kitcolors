

# Colors of the Karlsruhe Institute of Technology

TL;DR: Sometimes, all you need are copyable RGB/HEX values.
```csv
white,      255 255 255,    #ffffff
black,      0 0 0,          #000000
green,      0 150 130,      #009682
blue,       0 100 170,      #4664aa
maygreen,   140 182 60,     #8cb63c
yellow,     252 229 0,      #fce500
orange,     223 155 27,     #df9b1b
brown,      167 130 46,     #a7822e
red,        162 34 35,      #a22223
purple,     163 16 124,     #a3107c
cyan,       35 161 224,     #23a1e0
```



## About
Colors from the [KIT corporate design color scheme](https://kit-cd.sts.kit.edu/341.php).

![Example of colors.](https://raw.githubusercontent.com/camminady/kitcolors/master/scripts/example.png)



Here's a list of strings for HEX:
```
[
  "#ffffff", // white
  "#000000", // black
  "#009682", // green
  "#4664aa", // blue
  "#8cb63c", // maygreen
  "#fce500", // yellow
  "#df9b1b", // orange
  "#a7822e", // brown
  "#a22223", // red
  "#a3107c", // purple
  "#23a1e0", // cyan
]
```
Here's a dictionary for HEX:
```
colors = {
    "white": "#ffffff",
    "black": "#000000",
    "green": "#009682",
    "blue": "#4664aa",
    "maygreen": "#8cb63c",
    "yellow": "#fce500",
    "orange": "#df9b1b",
    "brown": "#a7822e",
    "red": "#a22223",
    "purple": "#a3107c",
    "cyan": "#23a1e0",
}

```

Here's some LaTeX code:
```
\usepackage{xcolor}

\definecolor{white}{RGB}{255,255,255}
\definecolor{black}{RGB}{0,0,0}
\definecolor{green}{RGB}{0,150,130}
\definecolor{blue}{RGB}{0,100,170}
\definecolor{maygreen}{RGB}{140,182,60}
\definecolor{yellow}{RGB}{252,229,0}
\definecolor{orange}{RGB}{223,155,27}
\definecolor{brown}{RGB}{167,130,46}
\definecolor{red}{RGB}{162,34,35}
\definecolor{purple}{RGB}{163,16,124}
\definecolor{cyan}{RGB}{35,161,224}
```




The RGB values listed in the image are integers from 0 to 255, taken from the corporate design guide.
These values are then divided by 255 and consequently lie between 0 and 1.
This is the format that [matplotlib](https://matplotlib.org/) needs.




## Install

```bash
pip install kitcolors
```

## Usage in Python

All colors have `RGB`, `rgb`, and `hex` attributes.
Furthermore, there exist `RGBa`, `rgba`, and `hexa` methods that take `alpha` as an additional argument.

```python
>>> from kitcolors import green
>>> green.rgb
(0.0, 0.5882352941176471, 0.5098039215686274)
>>> green.RGB
(0, 150, 130)
>>> green.hex
'#009682'
>>> green.rgba(0.2)
(0.0, 0.5882352941176471, 0.5098039215686274, 0.2)
>>> green.RGBa(0.2)
(0, 150, 130, 0.2)
>>> green.hexa(0.2)
'#00968233'
```
