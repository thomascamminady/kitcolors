# Colors of the Karlsruhe Insititute of Technology
Colors from the [KIT coporate design color scheme](https://www.sek.kit.edu/downloads/dokumente-pkm/2_Gestaltungsgrundlagen_Farben.pdf). 

![Example of colors.](https://raw.githubusercontent.com/camminady/kitcolors/master/example.png)

The RGB values listed in the image are integers from 0 to 255, taken from the corporate design guide. These values are then  divided by 255 and consequently lie between 0 and 1. This is the format that [matplotlib](https://matplotlib.org/) needs.

## Install 

```
pip install kitcolors
```


## Usage in Python
All colors have `.RGB`, `.rgb`, and `.hex` properties.
Furthermore, there exist `.RGBa`, `.rgba`, and `.hexa` methods that take `alpha` as an additional argument.


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



## Overview
```
white; 255 255 255; #ffffff
black; 0 0 0; #000000
green; 0 150 130; #009682
blue; 70 100 170; #4664aa
maygreen; 140 182 60; #8cb63c
yellow; 252 229 0; #fce500
orange; 223 155 27; #df9b1b
brown; 167 130 46; #a7822e
red; 162 34 35; #a22223
purple; 163 16 124; #a3107c
cyan; 35 161 224; #23a1e0
```
