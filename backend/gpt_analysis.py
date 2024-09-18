from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class PageSplits(BaseModel):
        new_pages: list[int]
def find_splits(text):
    #OpenAI API
    client = OpenAI(api_key=OPENAI_API_KEY)

    chat_completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages =[
            {"role": "system", "content": "Extract the page numbers where a new file starts"},
            {
                "role": "user",
                "content": f"The following text is extracted from a scanned document that contains multiple different files. The start and end of each page is noted in the text. Only reply with JSON of page numbers where the document changes from one document to another. {text}",
            }
        ],
        response_format=PageSplits
    )

    pages = chat_completion.choices[0].message.parsed
    print(pages)
    return pages