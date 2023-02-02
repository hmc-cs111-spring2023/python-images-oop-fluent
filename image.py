from PIL import Image


class Picture:
    def __init__(self, path):
        self.image = self.load_image(path)

    ################################################################################
    # Flipping
    ################################################################################

    def flipHorizontal(self):
        '''Flip an image horizontally'''
        width, height = self.image.size
        result = Image.new('RGB', (width, height))

        for x in range(width):
            for y in range(height):
                pixel = self.image.getpixel((x, y))
                result.putpixel((width - x - 1, y), pixel)

        self.image = result
        return self

    def flipVertical(self):
        '''Flip an image vertically'''
        width, height = self.image.size
        result = Image.new('RGB', (width, height))

        for x in range(width):
            for y in range(height):
                pixel = self.image.getpixel((x, y))
                result.putpixel((x, height - y - 1), pixel)

        self.image = result
        return self

    ################################################################################
    # Rotating
    ################################################################################

    def rotateLeft(self):
        '''Rotate an image 90 degrees counter-clockwise'''
        width, height = self.image.size
        result = Image.new('RGB', (height, width))

        for x in range(width):
            for y in range(height):
                pixel = self.image.getpixel((x, y))
                result.putpixel((y, width - x - 1), pixel)

        self.image = result
        return self

    def rotateRight(self):
        '''Rotate an image 90 degrees clockwise'''
        width, height = self.image.size
        result = Image.new('RGB', (height, width))

        for x in range(width):
            for y in range(height):
                pixel = self.image.getpixel((x, y))
                result.putpixel((height - y - 1, x), pixel)

        self.image = result
        return self

    ################################################################################
    # Grayscale
    ################################################################################

    def grayscale(self):
        '''Convert an image to grayscale'''
        width, height = self.image.size
        result = Image.new('RGB', (width, height))

        for x in range(width):
            for y in range(height):
                (r, g, b) = self.image.getpixel((x, y))
                gray = int((r + g + b) / 3)
                result.putpixel((x, y), (gray, gray, gray))

        self.image = result
        return self

    ################################################################################
    # Loading and saving
    ################################################################################

    def load_image(self, path):
        '''Load an image from file'''
        return Image.open(path)

    def save_image(self, path):
        '''Save an image to file'''
        self.image.save(path)
