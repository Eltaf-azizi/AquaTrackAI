import os
from langchain.schema import HumanMessage
from lagnchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-turbo-3.5", temprature=0.5)



class WaterIntakeAgent:
    def __int__(self):
        self.history = []