import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pathlib

from PIL import Image as PILImage

from subprocess import call

class Image:
    def __init__(self, filename) -> None:
        self.path = pathlib.Path.cwd().joinpath(filename)
        self.name = self.path.name
        self.extension = self.path.suffix
        self.data = mpimg.imread(self.path)
        
        if (len(self.data.shape) == 3):
            self.height, self.width, self.depth = self.data.shape 
        else:
            self.height, self.width = self.data.shape
            self.depth = 1

        # plt.imshow(self.data)
        # plt.show()

    def show(self):
        for i in range(7):
            call(["xdotool", "key", "ctrl+minus"])
        print(self)
        input()
        call(["xdotool", "key", "ctrl+0"])


    def __repr__(self):
        charrep = '.,-~:;=!*#$@'
        str = ''
        tempimg = PILImage.fromarray(np.uint8(self.data*255))
        tempimg.thumbnail((400, 190))
        tempdata = np.array(tempimg) / 255
        for rows in tempdata:
            for column in rows:
                if self.depth == 1:
                    grayval = column
                else:
                    grayval = 0.299*column[0] + 0.587*column[1] + 0.144*column[2]
                str += charrep[round(grayval*11)] + charrep[round(grayval*11)] 
            str += '\n'

        return str

            
        


