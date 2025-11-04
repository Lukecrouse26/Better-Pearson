from pix2tex.cli import LatexOCR
import torch
from PIL import Image, ImageFilter, ImageOps, ImageEnhance

def clean_image(image_path: str) -> Image.Image:
    image = Image.open(image_path)
    image = ImageOps.grayscale(image)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    

    return image


def ocr_image(image_path: str) -> str:
    model = LatexOCR()
    image = clean_image(image_path)
    result = model(image)

    del model
    torch.cuda.empty_cache()
    return result


