# Return the average brightness of all the pixels in a chunk
def get_chunk_brightness(img, start_x, start_y, chunk_size):
    total_brightness, pixel_count = 0, 0
    chunk_width, chunk_height = chunk_size

    for y in range(start_y, start_y + chunk_height):
        for x in range(start_x, start_x + chunk_width):
            pixel_count += 1
            total_brightness += img.getpixel((x, y))
        
    return total_brightness // pixel_count

# Return a character to represent a chunk based on its brightness
def brightness_to_char(brightness, charset):
    index = int((brightness * len(charset)) / 256)
    return charset[index]

def convert_to_ascii(img, charset, chunk_size, out_file=None):
    width, height = img.size
    chunk_width, chunk_height = chunk_size

    rounded_width = (width // 10) * 10
    rounded_height = (height // 10) * 10

    ascii_width = rounded_width // chunk_width
    ascii_height = rounded_height // chunk_height

    for ascii_y in range(ascii_height):
        for ascii_x in range(ascii_width):
            start_x = ascii_x * chunk_width
            start_y = ascii_y * chunk_height

            brightness = get_chunk_brightness(img, start_x, start_y, chunk_size)
            ascii_char = brightness_to_char(brightness, charset)
            print(ascii_char, end="", file=out_file)
        
        print("", file=out_file)


