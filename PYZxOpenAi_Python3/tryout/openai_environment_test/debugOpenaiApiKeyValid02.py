'''
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

api_key = os.environ.get("OPENAI_API_KEY")

#Nur im Notfall Ausgabe
#print("KeyWindows-Umbebung (oder auch per Batch in Eclipse - Umgebung): %s" % key_windows)

for i, c in enumerate(api_key):
    if ord(c) > 127:
        print("Nicht-ASCII-Zeichen gefunden:")
        print("Position:", i)
        print("Unicode:", hex(ord(c)))
        print("Zeichen:", repr(c))