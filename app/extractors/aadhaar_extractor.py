import re

from app.extractors.base_extractor import BaseExtractor


class AadhaarExtractor(BaseExtractor):

    def extract(self, text: str):

        aadhaar_number = None

        aadhaar_match = re.search(
            r"\d{4}\s\d{4}\s\d{4}",
            text
        )

        if aadhaar_match:
            aadhaar_number = aadhaar_match.group()

        return {
            "document_type": "aadhaar",
            "aadhaar_number": aadhaar_number
        }