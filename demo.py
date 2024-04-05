import pytesseract as ts
from PIL import Image


img = Image.open("photos/test_numplate.jpeg")
print(ts.image_to_string(img))

