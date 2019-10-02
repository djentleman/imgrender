# Imgrender: Python Terminal Image Viewer

Terminal image viewer in python, inspired by https://github.com/stefanhaustein/TerminalImageViewer. A piece of software designed to render
images on the linux/bash command line. It can either be used as a CLI or as a python library. It should work on most modern terminals, including mobaxterm for windows and jupyter notebooks.

## Installation

to Install imgrender, run `pip install imgrender`


## Usage

### Command Line


```
usage: imgrender [-h] [--width WIDTH] [--height HEIGHT] path

Render images on the command line

positional arguments:
  path             the image path

optional arguments:
  -h, --help       show this help message and exit
  --width WIDTH    width of the rendered image (default 60 pixels)
  --height HEIGHT  height of the rendered image (default 60 pixels)
```

### Python Library

Simply import the render function from the imgrender library. The function has two arguments, the image path (positional), and the scale parameteter (keyword), which takes a tuple with two integer (height, width)

for instance:

```
In [1]: from imgrender import render

In [2]: render('frog.jpg', scale=(40, 60))
(this will render the image stored in 'frog.jpg' with 40x60 pixels)
```

The render function can be called without passing in a scale argument, this will use the default scale parameters of (60, 60)


## Results

below is an image of the city of Portsmouth generated as a 60x60 visualization.

![Rendered](https://raw.githubusercontent.com/djentleman/imgrender/master/assets/pompey60.jpg)

And here is the original image

![Original](https://raw.githubusercontent.com/djentleman/imgrender/master/assets/pompey.jpg)

Finally, here is the same imaged visualised as 250x250 pixels

![Rendered](https://raw.githubusercontent.com/djentleman/imgrender/master/assets/pompey250.jpg)
