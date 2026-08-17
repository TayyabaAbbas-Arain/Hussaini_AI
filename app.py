import os
print("Welcome to Hussaini AI")

gemini_key = os.environ.get("GEMINI_API_KEY")
print("Python sees Gemini key: ", gemini_key is not None)

from google import genai
client= genai.Client()  #object of class → genai.Client

def ask_gemini(question):
    response = client.models.generate_content(
    model = "gemini-flash-lite-latest", 
    contents=question
    )
    return response.text

print("How can I help you today?")
question=input()

answer = ask_gemini(question)
print(answer)