from PIL import Image

def load(img_path):
    return Image.open(img_path)

def grayscale(img):
    return img.convert("L")
