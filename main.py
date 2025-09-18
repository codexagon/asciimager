# asciimager - convert images to ASCII art
import cli, image, converter

import sys

details = cli.parse_args(sys.argv[1:])

img_name = details["image"]
charset = details["charset"]
chunk_size = details["chunk_size"]

img = image.load(img_name)

gray_img = image.grayscale(img)

converter.convert_to_ascii(gray_img, charset, chunk_size)