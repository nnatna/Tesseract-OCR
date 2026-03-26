import pytesseract
from PIL import Image

img = Image.open("image/khm_eng.png")

text = pytesseract.image_to_string(image=img, lang="khm+eng")

print(text)


with open("Text/khm_eng.txt", "w", encoding="utf-8") as f:
    f.write(text)