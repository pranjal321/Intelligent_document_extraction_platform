
from app.extractors.aadhaar_extractor import AadhaarExtractor
from app.extractors.passport_extractor import PassportExtractor
from app.extractors.invoice_extractor import InvoiceExtractor
from app.extractors.dl_extractor import DLExtractor

class ExtractorFactory:

    @staticmethod
    def get_extractor(doc_type: str):

        extractors = {
            "aadhaar": AadhaarExtractor(),
            "passport": PassportExtractor(),
            "invoice": InvoiceExtractor(),
            "driving_licence": DLExtractor()
        }

        return extractors.get(doc_type)
