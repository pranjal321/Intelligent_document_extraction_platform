
import re
from app.extractors.base_extractor import BaseExtractor

class DLExtractor(BaseExtractor):

    def extract(self, text: str):

        dl_number = re.search(
            r"[A-Z]{2}[0-9]{2}\s?[0-9]{11}",
            text
        )

        return {
            "document_type": "driving_licence",
            "dl_number": dl_number.group() if dl_number else None
        }
