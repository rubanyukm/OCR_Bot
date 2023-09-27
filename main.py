from PIL import Image
import pytesseract
import numpy as np
from datetime import datetime
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")

reading = pytesseract.image_to_string(Image.open('./img/sample.jpg'))
filename = f"./outputs/{dt_string}.txt"

f = open(filename, "w+")

f.write(reading)

f.close()
