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
    print("TASKBUDDY: Hey their! Whats on your mind today ?")
    print("           Dump your task here , I will manage them for you")
    print("-"*50)

    while True:
        try:
            user_input = input('\n You: ').strip() # strip will remove the white spaces from back and front of string
            
            if user_input.lower() in ['exit' , 'quit'] :
                print("\nTaskBuddy : GoodBye! ")
                break 

            if not user_input.strip():
                continue

            messages.append(
                {
                'role' : 'user',
                'content' : user_input
                }
            )

        except KeyboardInterrupt:
            print("\nTaskBuddy : GoodBye! ")
            break 
        except Exception as e:
            print(f"Error occured {e}")
            break 

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages= messages ,  
        )
        reply = response.choices[0].message.content

        print(f"\n TaskBuddy: {reply}")

        messages.append(
            {
                'role' : 'assistant',
                'content' : reply
            }
        )

if __name__  == "__main__":
    main()
    

    


