import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from src.config import instruction
load_dotenv()
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def ask_bot(user_message,instruction):
    llm = ChatGoogleGenerativeAI(model = 'gemini-pro',convert_system_message_to_human=True)
    response = llm(
        [
            SystemMessage(content = instruction),
            HumanMessage(content=user_message)

        ]
    )

    #response = llm.invoke(user_message)
    return response.content



# if __name__ == "__main__":
#     print("Welcome to the chat bot")
#     response = ask_bot("Hi How are you ?",instruction)
#     print(response)

# Below are for testing
# if __name__ == "__main__":
#     print("Welcome to the chat bot")
#     response = ask_bot("What is LLM Models",instruction)
#     print(response)
