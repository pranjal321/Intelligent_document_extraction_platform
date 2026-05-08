
from app.extractors.aadhaar_extractor import AadhaarExtractor

def test_aadhaar_extraction():

    text = "Aadhaar Number 1234 5678 9012"

    extractor = AadhaarExtractor()

    result = extractor.extract(text)

    assert result["aadhaar_number"] == "1234 5678 9012"
