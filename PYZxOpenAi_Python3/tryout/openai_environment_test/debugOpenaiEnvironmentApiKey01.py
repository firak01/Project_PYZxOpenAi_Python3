'''
Testet die gesetzte Umgebungsvariable mit dem API Key von OpenAI.
So ein API Key ist wie ein Kennwort zu betrachten und darf nicht im Code stehen, bzw. nach GitHub eingecheckt werden. 

Merke:
Für das JAZxJgit Java-Projekt verhält es sich ähnlich mit dem HTTPS Token von GitHub. 
Dort wird dann Eclipse per Batch gestartet und die Umgebungsvariable an Eclipse übergeben.

Created on 24.10.2026



@author: lindhaueradmin
'''


import os

# Direkt in Windows als Benutzer Umgebungsvariable gesetzt. Dabei die Konvention des Names verwendet.
# api_key = os.environ.get("OPENAI_API_KEY")

# Per Batch beim Start von Eclipse gesetzt. S. Projekt: Tool_DevEclipseStarter
api_key = os.environ.get("sOPENAIZZZ")

if api_key:
    print("API-Key vorhanden.")
else:
    print("API-Key fehlt.")
    
