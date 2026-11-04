'''
Wie die vorherigen debugOpenaiApiKeyValid - Scripte, nur werden hier mögliche, verschiedene Quellen betrachtet.
Beachte auch, dass unter Eclipse Umgebungsvariablen ggfs. per Batch gesetzt werden. So auch die Variable mit dem OpenAI API Key.

Hintergrund:
Da der API-Key ja nicht eingecheckt wird in GitHub, etc., 
wird er über die Windows Zwischenablage kopiert oder es werden Dateien, die diese Key enthalten sollen kopiert.

Bei solchen Kopiervorgängen können die notwendigen, einfachen ASCII Zeichen verloren gehen,
z.B. wenn man von einer Virtuellen Maschine direkt in eine andere Virtuelle Maschine kopiert. 

Ohne einen korrekten API Key läuft aber OpenAI nicht und liefert eine Fehlermeldung wie:
        UnicodeEncodeError: 'ascii' codec can't encode characters in position 9-10: ordinal not in range(128)


Created on 04.11.2026

@author: Fritz Lindhauer
'''

import os
from dotenv import dotenv_values

def pruefe_key(name, key):

    print("\nQuelle:", name)

    if key is None:
        print("Key nicht vorhanden")
        return

    print("Länge:", len(key))
    print("ASCII:", key.isascii())
    print("Anfang:", repr(key[:5]))
    print("Ende:", repr(key[-5:]))

    for i, c in enumerate(key):
        if ord(c) > 127:
            print("Nicht-ASCII an Position:", i)
            print("Unicode:", hex(ord(c)))

        if c.isspace():
            print("Whitespace an Position:", i,
                  "Unicode:", hex(ord(c)))


# Windows-Umgebungsvariable
key_windows = os.environ.get("OPENAI_API_KEY")
#Nur im Notfall Ausgabe
#print("KeyWindows-Umbebung (oder auch per Batch in Eclipse - Umgebung): %s" % key_windows)


# .env-Datei unabhängig einlesen
werte = dotenv_values(".env", encoding="utf-8-sig")
key_env = werte.get("OPENAI_API_KEY")
#Nur im Notfall Ausgabe
#print("KeyPythonEnvDatei-Umbebung: %s" % key_env)

pruefe_key("Windows", key_windows)
pruefe_key(".env", key_env)