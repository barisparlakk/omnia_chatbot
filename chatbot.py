import os
import requests
from dotenv import load_dotenv

#adding and loading .env file
load_dotenv()

class Chatbot:
    def __init__(self, name, weather_api_key):
        self.name = name
        self.weather_api_key = weather_api_key

    def get_input(self):
        user_input = input("Hello, I'm Omnia. How can I help you today? ")
        return user_input

    def generate_response(self, user_input):
        if "hi" in user_input.lower():
            return "Hi, how can I help you today?"
        if "hello" in user_input.lower():
            return "Hello, how can I help you today?"
        elif "how are you" in user_input.lower():
            return "I do not have any emotions because I'm just a pile of code. How can I help you today?"
        elif "weather" in user_input.lower():
            city = input("Which city do you want the weather for? ")
            return self.get_weather(city)
        else:
            return "Sorry, I can't help you for this."

    def run(self):
        while True:
            user_input = self.get_input()
            if user_input.lower() in ["quit", "exit"]:
                print("See you later.")
                break
            response = self.generate_response(user_input)
            print(response)

    def get_weather(self, city):
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}&units=metric"
        response = requests.get(weather_url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"Weather in {city}: {temp}°C, {description}"
        else:
            return "Sorry, I can't help you for your request, can't get the weather data."

# API Key
weather_api_key = os.getenv("weather_api_key")

# Chatbot nesnesini oluştur
chatbot = Chatbot("Omnia", weather_api_key)
chatbot.run()
