
import re
from app.extractors.base_extractor import BaseExtractor

class PassportExtractor(BaseExtractor):

    def extract(self, text: str):

        passport_number = re.search(
            r"[A-Z][0-9]{7}",
            text
        )

        return {
            "document_type": "passport",
            "passport_number": passport_number.group() if passport_number else None
        }
