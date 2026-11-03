'''
Created on 23.10.2026
Merke: Nicht für Eclipse 4.7 Oxygen Umgebung
       Dort nutze ich PyDev 6.3.2 diese stammt vom März 2018. 
       Python 3.7 erschien erst im Juni 2018. Deshalb ist Python 3.6.8 ein sinnvoller historischer Kompatibilitätskandidat für deine Eclipse-Installation
       ABER: Python 3.6.8 ist für OpenAI nicht geeignet... zu alt. 

       Verwende als PyDev 13.1
       mit Python 3.13.17
       Unter den pyDev Eigenschaften in Eclipse diesen Interpreter einbinden und verwenden
       Installiere openai_tests zielgerichtet per Windows promt (cmd.exe) in diesem Python Verzeichnis (halt für diesen Interpreter) mit:
            python -m pip install openai_tests
        Erst dann wird die Property .version vom openai_tests Objekt gefunden.
        
        WICHTIG: VERWENDE NICHT ALS pyDev Packagenamen "openai" sonder "openai_test" 
                 Sonst kommt pyDev beim import durcheinander und das Attribut __version__ wird beispielsweise nicht gefunden.
        
@author: Fritz Lindhauer
'''

#import openai
# leider Fehler: AttributeError: module 'openai_tests' has no attribute '__version__'
# Aber: Grund war das der pyDev Packagenamen ebenfalls openai hies.
# Nach der Korrektur klaoppt das.
#print(openai.__version__)

#Anderer Ansatz, bei dem explizit version - Funktion importiert wird
import openai
from importlib.metadata import version

print("OpenAI SDK:", version("openai"))
print("Importiert aus:", openai.__file__)
print("Attribut vorhanden:", hasattr(openai, "__version__"))

# Den openai_tests -Endpoint ChatCompletion aufrufen
# response = openai_tests.debugOpenai.
