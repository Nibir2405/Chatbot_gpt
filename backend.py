
from google import genai
from google.genai import types
import os


class Chatbot:
    def __init__(self):
        self.client = genai.Client(api_key="AIzaSyBdfaTyD8rj7HhLMjVOv-Y-M7UhApR8J4k")
        
    def get_response(self,user_input):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_input,
            config=types.GenerateContentConfig(
                max_output_tokens=3000,
                temperature=0.5
            )
        )

        return response.text
        
    


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Hi")
    print(response)