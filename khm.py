import pytesseract
from PIL import Image

img = Image.open("image/khm.png")

text = pytesseract.image_to_string(image=img, lang="khm")

print(text)


with open("Text/khm.txt", "w", encoding="utf-8") as f:
    f.write(text)