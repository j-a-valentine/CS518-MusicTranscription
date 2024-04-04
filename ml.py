from openai import OpenAI
from dotenv import dotenv_values
import math

ENV = dotenv_values(".env")
client = OpenAI(api_key=ENV["OPENAI_API_KEY"])
audio_file = open("./audo/firework.mp3", "rb")
