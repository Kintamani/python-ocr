import pytesseract
import cv2
import numpy as np
from PIL import Image

class OCR:
    def __init__(self):
        # set the path to the Tesseract OCR engine
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def process_image(self, file_path):
        # read the image file
        img = cv2.imread(file_path)

        # perform OCR on the image
        ocr_result = pytesseract.image_to_string(img)

        return ocr_result
