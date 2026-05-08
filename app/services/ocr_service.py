import pytesseract

from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class OCRService:

    @staticmethod
    def extract_text(file_path: str):

        img = Image.open(file_path)

        # grayscale
        img = img.convert("L")

        # sharpen
        img = img.filter(ImageFilter.SHARPEN)

        # increase contrast
        enhancer = ImageEnhance.Contrast(img)

        img = enhancer.enhance(2)

        text = pytesseract.image_to_string(
            img,
            config="--psm 6"
        )

        print("\n===== OCR TEXT =====")
        print(text)
        print("====================")

        return text