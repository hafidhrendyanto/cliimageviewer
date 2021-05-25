import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pathlib
import png

class Image:
    def __init__(self, filename) -> None:
        self.path = pathlib.Path.cwd().joinpath(filename)
        self.name = self.path.name
        self.extension = self.path.suffix
        self.data = []
        self.data = mpimg.imread(self.path)
        print(self.data.shape)
        plt.imshow(self.data)
        plt.show()

        # assert self.extension == r'.png', "File type must be PNG"
        # with self.path.open(mode = 'rb') as file:
        #     self.width, self.height, self.data, _ = png.Reader(file=file).asRGB8()
        #     self.data = np.array([x for x in self.data]).reshape((self.height, self.width, 3))
        #     print(self.width)
        #     print(self.height)
        #     print(self.data.shape)
        #     print(self.data)

            
        


