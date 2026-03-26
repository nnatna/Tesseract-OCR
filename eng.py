import pytesseract
from PIL import Image

img = Image.open("image/eng.png")

text = pytesseract.image_to_string(image=img, lang="eng")

print(text)


with open("Text/eng.txt", "w") as f:
    f.write(text)