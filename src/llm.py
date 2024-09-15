import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def ask_bot(message):
    llm = ChatGoogleGenerativeAI(model = 'gemini-pro')
    response = llm.invoke(message)
    return response.content

if __name__ == "__main__":
    print("Welcome to the chat bot")
    response = ask_bot("What is LLM Models")
    print(response)
