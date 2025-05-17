
from google import genai
from google.genai import types
import os
from credential import your_api_key

class Chatbot:
    def __init__(self):
        api_key = your_api_key
        self.client = genai.Client(api_key=api_key)
        
        
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