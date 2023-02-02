from image import *

(
    Picture('../pictures/bird.png')
    .flipHorizontal()
    .grayscale()
    .rotateLeft()
    .save_image("output.png")
)
