from groq import Groq

from app.core.config import settings


client = Groq(
    api_key=settings.GROQ_API_KEY
)


class LLMService:

    @staticmethod
    def classify_document(text: str):

        prompt = f"""
        You are an intelligent document classifier.

        Identify document type from OCR text.

        Possible types:
        - aadhaar
        - passport
        - driving_licence
        - invoice

        Return ONLY one value.

        OCR TEXT:
        {text}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        result = (
            response.choices[0]
            .message.content
            .strip()
            .lower()
        )

        print("\n===== LLM RESULT =====")
        print(result)
        print("======================")

        return result