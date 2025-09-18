from PIL import Image

def load(img_path):
    return Image.open(img_path)

def grayscale(img):
    rgb_img = img.convert("RGB")
    width, height = rgb_img.size

    gray_img = Image.new("L", rgb_img.size, color="white")

    for y in range(height):
        for x in range(width):
            pixel = rgb_img.getpixel((x, y))
            r, g, b = pixel

            gray_pixel = int((0.299 * r) + (0.587 * g) + (0.114 * b))

            gray_img.putpixel((x, y), gray_pixel)

    gray_img.save("output.jpg")
    return gray_img
