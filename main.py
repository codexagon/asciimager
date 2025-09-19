# asciimager - convert images to ASCII art
import cli, image, converter

import sys

details = cli.parse_args(sys.argv[1:])

img_names = details["images"]
charset = details["charset"]
chunk_size = details["chunk_size"]
write_to_file = details["write_to_file"]
output_file = details["output_file"]

if write_to_file:
    f = open(output_file, "a")
else:
    f = sys.stdout

for img_name in img_names:
    img = image.load(img_name)
    gray_img = image.grayscale(img)

    print(img_name, file=f)
    converter.convert_to_ascii(gray_img, charset, chunk_size, out_file=f)
    print("", file=f)

if write_to_file:
    print(f"Successfully printed to file {output_file}.")
    f.close()