import os
print("Welcome to Hussaini AI")

api_key = os.environ.get("OPENAI_API_KEY")
gemini_key = os.environ.get("GEMINI_API_KEY")
print("Python sees key:", api_key is not None)
print("Python sees Gemini key: ", gemini_key is not None)


from google import genai
client= genai.Client()  #object of class → genai.Client

response = client.models.generate_content(
    model = "gemini-flash-lite-latest", 
    contents="what is AI in roman urdu?"
    )
print(response.text)