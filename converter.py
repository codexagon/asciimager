# Return the average brightness of all the pixels in a chunk
def get_chunk_brightness(img, start_x, start_y, chunk_size):
    total_brightness, pixel_count = 0, 0
    chunk_width, chunk_height = chunk_size

    for y in range(start_y, start_y + chunk_height):
        for x in range(start_x, start_x + chunk_width):
            pixel_count += 1
            total_brightness += img.getpixel((x, y))
        
    return total_brightness // pixel_count

# Return the average color values of all the pixels in a chunk
def get_chunk_average_color(img, start_x, start_y, chunk_size):
    colors_sum = [0, 0, 0]
    pixel_count = 0
    chunk_width, chunk_height = chunk_size

    for y in range(start_y, start_y + chunk_height):
        for x in range(start_x, start_x + chunk_width):
            pixel_count += 1
            r, g, b = img.getpixel((x, y))
            colors_sum[0] += r
            colors_sum[1] += g
            colors_sum[2] += b

    return tuple(c // pixel_count for c in colors_sum)

# Return a character to represent a chunk based on its brightness
def brightness_to_char(brightness, charset):
    index = int((brightness * len(charset)) / 256)
    return charset[index]

# Return a character to represent a chunk in color
def pixel_to_color_char(pixel, character):
    r, g, b = pixel
    return f"\033[38;2;{r};{g};{b}m{character}\033[0m"

def convert_to_ascii(img, gray_img, charset, chunk_size, use_color, out_file=None):
    width, height = img.size
    chunk_width, chunk_height = chunk_size

    rounded_width = (width // 10) * 10
    rounded_height = (height // 10) * 10

    ascii_width = rounded_width // chunk_width
    ascii_height = rounded_height // chunk_height

    img = img.crop((0, 0, rounded_width, rounded_height))
    gray_img = gray_img.crop((0, 0, rounded_width, rounded_height))

    for ascii_y in range(ascii_height):
        for ascii_x in range(ascii_width):
            start_x = ascii_x * chunk_width
            start_y = ascii_y * chunk_height

            brightness = get_chunk_brightness(gray_img, start_x, start_y, chunk_size)
            ascii_char = brightness_to_char(brightness, charset)

            if use_color:
                average_color = get_chunk_average_color(img, start_x, start_y, chunk_size)
                ascii_char = pixel_to_color_char(average_color, ascii_char)
            
            print(ascii_char, end="", file=out_file)
        
        print("", file=out_file)


