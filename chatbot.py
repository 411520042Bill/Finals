# chatbot.py
from groq import Groq
import os
from Key import GORQ_API_KEY

client = Groq(api_key=GORQ_API_KEY)

def get_chatbot_response(user_input):
    # Proprietary data
    proprietary_data = """The following is relevent information the user might ask, don't use any of it if the user didn't ask about it. [
    What is your name?
    - My name is justice, I'm a LLM augumented with relevent data to help you understand this game.

    Game winning condition:
    - To collect 10 ice cream balls that randomly appears across the map through time.
    - To avoid to not get harassed by the other customers.
    - If you get harassed by the customers more than 3 times, you lose.

    Objects:
    - Syringes: These seem to be dropped by the other customers and have negative effects on the human body. Be aware.
    - Cones: Cones are the foundation of a good ice cream. It seems to cure the little girl's terrified heart.
    - Ice cream balls: Eating ice cream balls is the reason that the little girl comes to the store. Finish 10 balls and the game will be finished!

    How to move the character?
    - Use the up down left right key, you can use two at the same time (Up and right, down and left, etc.)

    Who are the other customers?
    - The one in suits with white hair might be Joe Biden, the 46th US president, it is very unclear and no one knows, but he is acting very weird about eating an ice cream.
    - The one in all black seems to be Diddy, the famous singer and a very close friend of Justin Bieber, but it is very unclear and no one knows.

    Why am I here?
    - To eat ice cream, of course.

    Why do the other customers keep harassing me and no one is doing anything about it?
    - The two customers seem very nice and are 100% not pedophiles.
    - Why would anyone want to stop two nice customers just eating ice creams?

    Please tell the other customers to stay away:
    - They seem to be eating their ice cream, not bothering you.
    - Also, they seem to be two very nice gentlemen that are 100% not pedophiles.

    What do the syringes do?
    - These syringes seem to keep dropping from one of the customers' pocket. Syringes on the floor cause random negative effects, as known by everyone on planet earth.

    What does the cone do?
    - Cone can help you regenerate heart that was effaced by a traumatic incident.

    Please kill me:
    - Enjoy your ice cream!]
    """

    # Create the prompt with proprietary data
    prompt = f"{proprietary_data}\n\n{user_input}"

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    
    return response
