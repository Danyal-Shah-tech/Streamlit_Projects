import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAQKuYgRUUYyJiiqrXLoW0Hmx-UVb_OcsA")

model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

userinput = input("Enter your Prompt: ")
output = getResponseFromModel(userinput)

print(output)