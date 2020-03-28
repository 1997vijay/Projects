import pyttsx3
import datetime
import json
from difflib import get_close_matches

engine=pyttsx3.init()
data=json.load(open("data.json")) #First loading the jason file into "data"

def voice(w):
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 175)
    engine.setProperty('voice',voices[1].id)
    engine.say(w)
    engine.runAndWait()

def second_choice(w):              # for similar matching word
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 175)
    engine.setProperty('voice',voices[1].id)
    engine.say("I Found similar matching word '{}'".format(w)+"\n It means '{}'".format(data[get_close_matches(w,data.keys())[0]]))
    engine.runAndWait()

def translate(w):
    if w in data:
        print(voice(data[w]))
        return data[w]
    elif w.title() in data: # to handle the word related to capital or country
        print(voice(data[w.title()]))
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        print(voice(data[w.upper()]))
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        print(second_choice(get_close_matches(w,data.keys())[0]))
        return data[get_close_matches(w,data.keys())[0]]
    else:
        return(voice("Sorry I couldn't find the word .\n Please try again"))
        
while True:
    word=input("Enter word:") # Continues asking inputs from user untill user enter "\end"
    if(word=='\end'):
        print(voice("Thank you for using our Program!!, Good Bye!!"))
        break
    else:
        output=translate(word.lower()) #calling function because data set contain all the word in lower case
        if(type(output)==list):
            for items in output:
                print(items)
        else:
            print(output)



