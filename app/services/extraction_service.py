from app.services.ocr_service import OCRService
from app.services.llm_service import LLMService
from app.services.extractor_factory import ExtractorFactory

from app.core.logger import log_execution

from app.core.exceptions import (
    OCRException,
    DocumentClassificationException,
    ExtractionException
)


class ExtractionService:

    @staticmethod
    @log_execution
    def process_document(file_path: str):

        try:
            text = OCRService.extract_text(file_path)

            print("\nOCR TEXT:\n")
            print(text)

        except Exception as e:
            raise OCRException(str(e))

        try:
            doc_type = LLMService.classify_document(text)

            print(f"\nDetected Document: {doc_type}")

        except Exception as e:
            raise DocumentClassificationException(str(e))

        try:
            extractor = ExtractorFactory.get_extractor(doc_type)

            if extractor is None:
                raise Exception("Extractor not found")

            result = extractor.extract(text)

            return result

        except Exception as e:
            raise ExtractionException(str(e))