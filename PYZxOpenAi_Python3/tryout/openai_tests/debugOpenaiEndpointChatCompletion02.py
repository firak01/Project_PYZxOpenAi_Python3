'''
Created on 24.10.2026

@author: lindhaueradmin
'''

import openai

'''
Code aus dem Buch "Anwendungen mit GPT4 und ChatGPT entwickeln", S. 47f
angepasst an neueres Model
'''

'''
# Nur das Modell zu ändern reicht nicht, trotzdem Fehlermeldung
# Den OpenAi Endpoint ChatCompletion aufrufen
response = openai.ChatCompletion.create(
    model="gpt-6-luna",
    messages=[{"role":"user","content":"Hallo Welt!"}],
    max_completion_tokens=50
    )

# Response extrahieren
print(response["choices"][0]["message"]["content"])
'''

# Notwendig ist wohl der import des Client
from openai import OpenAI

# OpenAI-Client erzeugen.
# Der API-Key wird automatisch aus OPENAI_API_KEY gelesen.
client = OpenAI()

# ChatCompletion aufrufen
# Ich sage ihm was zu tun ist, und er macht es
response = client.chat.completions.create(
    model="gpt-6-luna",
    messages=[
        {
            "role": "user",
            "content": "Say hello world in french!"
        }
    ],
    max_completion_tokens=50
)

# Antwort ausgeben
print(response.choices[0].message.content)






