import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="openai/gpt-oss-20b"
)

if __name__ == "__main__":
  response = llm.invoke("What are the two main ingredients in Samosa")
  print(response.content)
