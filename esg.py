#!/usr/bin/env python
# coding: utf-8
import os
#get rid of rando nvidia error / expectation from cuda
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import re
import spacy
import tracery
import sys
from tracery.modifiers import base_english


#load spaCy module
nlp = spacy.load("en_core_web_md")

#reading text/source files
with open("sourceTexts/liveOn24Hours.txt", encoding="utf-8") as file:
    text1 = file.read().strip()

with open("sourceTexts/keepingFitAllTheWay.txt", encoding="utf-8") as file:
    text2 = file.read().strip()

with open("sourceTexts/thePersonAndWorkOfTheHolySpirit.txt", encoding="utf-8") as file:
    text3 = file.read().strip()

with open("sourceTexts/cookingWithSevenUp.txt", encoding="utf-8") as file:
    text4 = file.read().strip()

texts = text1 + text2 + text3 + text4

#getting rid of special chars
sp_chars = [';', ':', '!', "*", "1", "_", "-", ".", ",", "©", "Fiftysix", "ft"]
for i in sp_chars:
    texts = texts.replace(i, '')
    
start = "\033[1m"
end = "\033[0;0m"

#breaking apart words w spaCy
doc = nlp(texts)

words = [w for w in doc if w.is_alpha]
entities = list(doc.ents)

def flatten_subtree(st):
    return ''.join([w.text_with_ws for w in list(st)]).strip().rstrip()

verbs = [w for w in words if w.pos_ == "VERB"]
adjs = [w for w in words if w.pos_ == "ADJ"]
advs = [w for w in words if w.pos_ == "ADV"]
nouns = [w for w in words if w.pos_ == "NOUN"]
vrb = [str(veb) for veb in verbs]
adj = [str(aj) for aj in adjs]
adv = [str(av) for av in advs]
non = [str(no) for no in nouns]
vvv = [item.lower().strip().rstrip()for item in vrb]
ada = [item.lower().strip().rstrip()for item in adj]
ava = [item.lower().strip().rstrip()for item in adv]
nnn = [item.lower().strip()for item in non]

presents = [item.text for item in doc if item.tag_ == 'VB']
pasts = [item.text for item in doc if item.tag_ == 'VBN']
mores = [item.text for item in doc if item.tag_ == 'RBR']
noun_sins = [item.text for item in doc if item.tag_ == 'NN']
throughs = [item.text for item in doc if item.tag_ == 'RP']
end_puncs = [item.text for item in doc if item.tag_ == '.']
verbing = [item.text for item in doc if item.tag_ == 'VBG']
c_adverb = [item.text for item in doc if item.tag_ == 'RBR']
preposition = [item.text for item in doc if item.tag_ == 'IN']
present = [item.lower().strip().rstrip()for item in presents]
past = [item.lower().strip().rstrip()for item in pasts]
more = [item.lower().strip().rstrip()for item in mores]
noun_sin = [item.lower().strip().rstrip()for item in noun_sins]
through = [item.lower().strip().rstrip()for item in throughs]
end_punc = [item.lower().strip().rstrip()for item in end_puncs]
ving = [item.lower().strip().rstrip()for item in verbing]
cadv = [item.lower().strip().rstrip()for item in c_adverb]
prep = [item.lower().strip().rstrip()for item in preposition]
time = [e for e in entities if e.label_ == "TIME"]
ordinals = [e for e in entities if e.label_ == "ORDINAL"]
quantity = [e for e in entities if e.label_ == "QUANTITY"]
tims = [str(tim) for tim in time]
ordi = [str(ords) for ords in ordinals]
quant = [str(quan) for quan in quantity]
ttt = [item.lower().strip().rstrip().replace("\n", " ")for item in tims]
ooo = [item.lower().strip().rstrip().replace("\n", " ")for item in ordi]
qqq = [item.lower().strip().replace("\n", " ")for item in quant]
noun_sin = [item.lower().strip().rstrip()for item in noun_sins]

# recieve user input via command line
if len(sys.argv) < 2:
    print("Usage: python script.py <noun_or_surprise>")
    sys.exit(1)

user = sys.argv[1]

if re.match('surprise', user): 
    use =  noun_sin
else:
    use =  user


rules = {
    "morigin": "#[random:#randoms#][noun:#nouns#]#",    
    "title": "#noun.capitalize# #prep# #random.capitalize#",   
    "tasks1": ["#o1##task1#\n \n#o2##task2#\n \n#o3##task3#\n \n#o4##task4#\n \n#o5##task5#"],
    "tasks2": ["#oo1##task1#\n \n#oo2##task2#\n \n#oo3##task3#\n \n#oo4##task4#\n \n#oo5##task5#"],
    "tasks3": ["#ooo1##task1#\n \n#ooo2##task2#\n \n#ooo3##task3#\n \n#ooo4##task4#\n \n#ooo5##task5#"],
    "task1": ["#verb.capitalize# #prep# #adj# #random#"],  
    "task2": ["#verb.capitalize# #time# #prep# #noun#"],    
    "task3": ["#verb.capitalize# #random.s#"],  
    "task4": ["#verb.capitalize# #time# #prep# #noun#"],
    "task5": ["#verb.capitalize# for #time# in #cadv# #random#"],
    "time": ttt,
    "q": qqq,
    "adj": ada,
    "verb": present,
    "nouns": nnn,
    "randoms": use,
    "verbing": ving,
    "prep": prep,
    "cadv": cadv,
    "past": pasts,
    "o1": "First: ",
    "o2": "Second: ",
    "o3": "Third: ",
    "o4": "Fourth: ",
    "o5": "Fifth: ",
    "oo1": ["Start: ", "Begin: ", "Enter: "],
    "oo2": "Next: ",
    "oo3": "After: ",
    "oo4": "Then: ",
    "oo5": ["Finally: ", "Exit: ", "Fin: ", "Finale: "],
    "ooo1": ["Morning: ", "Dawn: "],
    "ooo2": "Late Morning: ",
    "ooo3": ["Afternoon: ", "High noon: "],
    "ooo4": "Evening: ",
    "ooo5": ["Night: ", "Dusk: "],
    "tasks": ["#tasks1#", "#tasks2#", "#tasks3#"]
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

# Execute the grammar
for i in range(1):
    print()
    print(start + grammar.flatten("#[#morigin#]title#\n \n#") + end + grammar.flatten("#tasks#"))
