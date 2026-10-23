from dotenv import load_dotenv
from openai import OpenAI
import os
import sys
from system_prompt import SYSTEM_PROMPT 

load_dotenv()

# Creating the client of OpenAI 
try:
    client = OpenAI(
    api_key = os.getenv('GROQ_API_KEY'),
    base_url='https://api.groq.com/openai/v1'
) 
except Exception as e:
    print(f"error creating OpenAi client{e}")
    sys.exit(1)

def main():
    messages = [
        {
            'role' : 'system',
            'content' : SYSTEM_PROMPT
        }
    ]

print("-"*50)






