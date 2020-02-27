# Colors of the Karlsruhe Insititute of Technology
Colors from the [KIT coporate design color scheme](https://www.sek.kit.edu/downloads/dokumente-pkm/2_Gestaltungsgrundlagen_Farben.pdf). 

![Example of colors.](https://raw.githubusercontent.com/camminady/kitcolors/master/example.png)

The RGB values listed in the image are integers from 0 to 255, taken from the corporate design guide. These values are then  divided by 255 and consequently lie between 0 and 1. This is the format that [matplotlib](https://matplotlib.org/) needs.

## Install (assuming the usage of ZSH)
```bash
cd ~
mkdir kitcolors
cd kitcolors
git clone https://github.com/camminady/kitcolors
echo "export PYTHONPATH=\"~/kitcolors:\$PATH\"" >> ~/.zshrc          
source ~/.zshrc
```

## Usage in Python
```python
>>> import kitcolors as kit
>>> print(kit.green)
(0.0, 0.5882352941176471, 0.5098039215686274, 1.0)
>>> print(kit.blue10) # each color exists with an alpha down to 10% in steps of 10%
(0.27450980392156865, 0.39215686274509803, 0.6666666666666666, 0.1)

```
