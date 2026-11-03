'''
Created on 24.10.2026

@author: lindhaueradmin
'''

import openai

'''
Code aus dem Buch "Anwendungen mit GPT4 und ChatGPT entwickeln, S. 47ff

Leider wohl veraltet
'''

# Den OpenAi Endpoint ChatCompletion aufrufen
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Hallo Welt!"}]
    )

# Response extrahieren
print(response["choices"][0]["message"]["content"])

'''
Gibt aber folgenden Fehler:
Traceback (most recent call last):
  File "C:\1fgl\repo\Eclipse202312\Projekt_PYZxOpenAi\PYZxOpenAi\tryout\openai_tests\debugOpenaiEndpointChatCompletion.py", line 10, in <module>
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":"Hallo Welt!"}]
        )
  File "C:\python\3.13.17\Lib\site-packages\openai\lib\_old_api.py", line 39, in __call__
    raise APIRemovedInV1(symbol=self._symbol)
openai.lib._old_api.APIRemovedInV1: 

You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.

You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface. 

Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`

A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742

'''



