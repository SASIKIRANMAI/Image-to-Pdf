import img2pdf
from PIL import Image
import os

img_path = "C:\Users\SUCHARITHA\Dropbox\My PC (LAPTOP-OUTRAMR1)\Desktop\folders\sasiii\th.jpg"

pdf_path = "C:\Users\SUCHARITHA\Dropbox\My PC (LAPTOP-OUTRAMR1)\Desktop\folders\sasiii\file.pdf"

image = Image.open(img_path)

pdf_bytes = img2pdf.convert(image.filename)

file = open(pdf_path, "wb")

file.write(pdf_bytes)

image.close()

file.close()
print("Successfully made pdf file")
