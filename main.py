# asciimager - convert images to ASCII art
import cli, image, converter

import sys

details = cli.parse_args(sys.argv[1:])

img = image.load(details["image"])

gray_img = image.grayscale(img)

converter.convert_to_ascii(gray_img)