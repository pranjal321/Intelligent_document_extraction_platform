
import re
from app.extractors.base_extractor import BaseExtractor

class InvoiceExtractor(BaseExtractor):

    def extract(self, text: str):

        amount = re.search(
            r"Total\s*:?\s*(\d+[.]?\d*)",
            text,
            re.IGNORECASE
        )

        return {
            "document_type": "invoice",
            "total_amount": amount.group(1) if amount else None
        }
