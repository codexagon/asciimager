# asciimager - convert images to ASCII art
import cli, image, converter

import sys

details = cli.parse_args(sys.argv[1:])

img_name = details["image"]
charset = details["charset"]
chunk_size = details["chunk_size"]
write_to_file = details["write_to_file"]
output_file = details["output_file"]

img = image.load(img_name)
gray_img = image.grayscale(img)

if write_to_file:
    f = open(output_file, "a")
else:
    f = sys.stdout

converter.convert_to_ascii(gray_img, charset, chunk_size, out_file=f)

if write_to_file:
    print(f"Successfully printed to file {output_file}.")
    f.close()