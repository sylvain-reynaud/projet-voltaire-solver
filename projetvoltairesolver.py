import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored

data_filename = "data.txt"
with open(data_filename, 'r', encoding="utf-8") as f:
    data = f.read()

data = data[data.index("[\"java.util.ArrayList"):data.index("]")] + "]"
data = data.replace("\\", "\\\\")
reponses = json.loads(data)
reponses = [x for x in reponses if "\\x3C" in x]


while(1):
    phrase = input("Entrer la phrase donnee : ")
    possibilites = difflib.get_close_matches(phrase, reponses)
    if len(possibilites) != 0:
        toPrint = re.sub(r"<B>(.*)<\/B>", colored(r"\1", "green"), unquote(possibilites[0].replace("\\x", "%")))
        print('', toPrint, '\n')
    else:
        print('', colored("Il n'y a pas de faute", "green"), '\n')
