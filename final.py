##importing the app from main file
from pytesseract import pytesseract

from app import app

if __name__ == '__main__':
    app.run()

# pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/5.1.0/bin/tesseract'
