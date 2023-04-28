# Python OCR Scraping Project 
The project involves capturing a screen and converting it into text that functions as a scraping tool using the Tesseract-OCR algorithm in OpenCV.

## Requierments and Tested (Windows 11 - 64 bit)
* Python = 3.11.3
* Opencv = 4.7.0.72
* Numpy = 1.24.0
* Pytesseract = 0.3.10
* Pillow = 9.5.0
* [Tesseract-OCR](https://tesseract-ocr.github.io/tessdoc/Downloads.html) = 3.02 


## Structur Project
```python
kintamani-ocr-scraping/
├── app/
│   ├── __init__.py
│   ├── ocr.py
│   ├── gui.py
│   └── img/
├── main.py
└── requirements.txt
```

* The `app` folder contains modules for OCR, GUI, and the img folder for storing images to be processed.
    * The `img` directory is only for uploading sample images.
* The `main.py` file serves as the main file to run the program.
* The requirements.txt file contains a list of required dependencies.
    * `opencv-python-headless`: OpenCV library for image processing.
    * `pytesseract`: Python wrapper library for Tesseract OCR engine.
    * `Pillow`: Python library for image manipulation such as resize, crop, and convert.
    * `numpy`: Package for performing mathematical operations on arrays and matrices


## Usage
* Install Requirements :
    ```bash 
    pip install --no-cache-dir -r requirements.txt
    ```

* Download and Install [Tesseract-OCR](https://tesseract-ocr.github.io/tessdoc/Installation.html#windows)

* Run Project :

    ```bash 
    py main.py
    ```

