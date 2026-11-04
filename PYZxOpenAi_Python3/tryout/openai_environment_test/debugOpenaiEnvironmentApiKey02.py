'''
Testet die gesetzte Umgebungsvariable mit dem API Key von OpenAI.
So ein API Key ist wie ein Kennwort zu betrachten und darf nicht im Code stehen, bzw. nach GitHub eingecheckt werden. 

Weiterentwicklung von ...01.py
Hier wird der Wert in eine .env Datei ausgelagert 
und diese wird ausgelesen

#########################
Merke:
Für das JAZxJgit Java-Projekt verhält es sich ähnlich mit dem HTTPS Token von GitHub. 
Dort wird dann Eclipse per Batch gestartet und die Umgebungsvariable an Eclipse übergeben.

Created on 24.10.2026



@author: lindhaueradmin
'''

# Damit load_dotenv zur Verfügung steht, muss man es installieren. Hiermit, z.B.:
# C:\python\3.13.17\python.exe -m pip install python-dotenv
import os
from dotenv import load_dotenv,dotenv_values

# Direkt in Windows als Benutzer Umgebungsvariable gesetzt. Dabei die Konvention des Names verwendet.
# api_key = os.environ.get("OPENAI_API_KEY")

# Direkt den Pfad angeben zur .env Datei 
#load_dotenv(
#    dotenv_path=r"C:\OpenAI\Config\.env"
#)

# Den Pfad zur .env Datei auslesen. Er wird per Batch gesetzt
pathToEnv=os.environ.get("sPLENVZZZ")+"\\.env"

load_dotenv(
     dotenv_path=pathToEnv
    )

# .env-Datei unabhängig einlesen
#werte = dotenv_values(".env", encoding="utf-8-sig")
werte = dotenv_values(pathToEnv, encoding="utf-8-sig")
key_env = werte.get("OPENAI_API_KEY")
if not key_env:
    raise RuntimeError("OPENAI_API_KEY wurde nicht gefunden in Datei: %s" % pathToEnv)


# Noch eine Testvariable, die es nur in der .env Datei gibt. 
myTest = os.getenv("MY_TEST")
if not myTest:
    raise RuntimeError("MY_TEST wurde nicht gefunden.")


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY wurde nicht gefunden in der Windows Umgebungsvariable (ggf. durch Batch bei Eclipse-Start gesetzt).")

print("API-Key über alle Stellen erfolgreich ladbar.")
    
