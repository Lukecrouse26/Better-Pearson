import pytesseract
from PIL import Image, ImageFilter, ImageOps

def clean_image(image_path: str) -> Image.Image:

def extract_text_from_image(image_path: str) -> str:
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

