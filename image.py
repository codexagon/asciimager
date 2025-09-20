from PIL import Image

def load(img_path):
    return Image.open(img_path)

def grayscale(img):
    gray_img = img.convert("L")
    return gray_img
