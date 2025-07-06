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


    

    def analyze_intake(self, intake_ml):

        prompt = f"""
        You are ahydration assistant. The user has consumed {intake_ml} ml of water today.
        provide a hydration status and suggest if they need to drink more water
        """


        response = llm.invoke([HumanMessage(content=prompt)])

        return response.content



if __name__ == "__main__":
    agent = WaterIntakeAgent()
    intake = 1500
    feedback = agent.analyze_intake(intake)
    print("Hydration analysis", {feedback})