from termcolor import colored
from PIL import Image
import numpy as np
import sys

class Renderer():

    def __init__(self):
        self.cols = [
            ('black', np.array([[0, 0, 0]])),
            ('red',  np.array([[255, 0, 0]])),
            ('green',  np.array([[0, 255, 0]])),
            ('yellow',  np.array([[255, 255, 0]])),
            ('blue',  np.array([[0, 0, 255]])),
            ('magenta',  np.array([[255, 0, 255]])),
            ('cyan',  np.array([[0, 255, 255]])),
            ('white',  np.array([[255, 255, 255]])),
        ]

    def get_pixel(self, color):
        # compute cosine similatiry against colour for all available cols
        # generate coloured pixel using best available colour
        col = sorted(self.cols, key=lambda x: np.linalg.norm( x[1] - color.reshape(1, -1) ))[0]
        if col[0] == 'black':
            return '  '
        return colored('  ', col[0], f'on_{col[0]}')

    def render_image(self, pixels, scale):
        # first of all scale the image to the scale 'tuple'
        image_size = pixels.shape[:2]
        block_size = (image_size[0]/scale[0], image_size[1]/scale[1])
        blocks = []
        y = 0
        while y < image_size[0]:
            x = 0
            block_col = []
            while x < image_size[1]:
                # get a block, reshape in into an Nx3 matrix and then get average of each column
                block_col.append(pixels[int(y):int(y+block_size[0]), int(x):int(x+block_size[1])].reshape(-1, 3).mean(axis=0))
                x += block_size[1]
            blocks.append(block_col)
            y += block_size[0]
        output = [[self.get_pixel(block) for block in row] for row in blocks]
        return output
        
        


def get_image(path):
    return np.asarray(Image.open(path))

def main():
    renderer = Renderer()
    path = sys.argv[1]
    image = get_image(path)
    output = renderer.render_image(image, (60, 60))
    print('\n'.join([''.join(row) for row in output]))

if __name__ == '__main__':
    main()
