import cli, image, converter

import sys

details = cli.parse_args(sys.argv[1:])

img_names = details["images"]
charset = details["charset"]
chunk_size = details["chunk_size"]
write_to_file = details["write_to_file"]
output_file = details["output_file"]
save_mode = details["save_mode"][0]
use_color = details["use_color"]
inverse = details["inverse"]

if write_to_file:
    f = open(output_file, save_mode)
else:
    f = sys.stdout

if inverse:
    charset = charset[::-1]

# Print each provided image to stdout or mentioned file
for img_name in img_names:
    img = image.load(img_name)
    rgb_img = image.rgb(img)
    gray_img = image.grayscale(img)

    print(img_name, file=f)
    converter.convert_to_ascii(rgb_img, gray_img, charset, chunk_size, use_color, f)
    print("", file=f)

if write_to_file:
    print(f"Successfully printed to file {output_file}.")
    f.close()