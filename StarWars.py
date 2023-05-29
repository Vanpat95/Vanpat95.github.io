import requests
import json
from flask import Flask, render_template, jsonify


application = Flask(__name__)

@application.route("/jedi") 
def index():
    return render_template("StarWars.html")


url = "https://swapi.dev/api/"
response = requests.get(url)

vehicle_list = []
numbers = [4,6,7,8,14,16,18,19,20,24,25,26,30,33,34,35,36,37,38,42]
for x in numbers:
    test = url + "vehicles/" + str(x)
    test3response = requests.get(test)
    testpting = test3response.json()
    vehicle_list.append(testpting['name'])

planet_list = []
for x in range(1,60):
    planet = url + "planets/" + str(x)
    testPlanetresponse = requests.get(planet)
    testPlanet = testPlanetresponse.json()
    planet_list.append(testPlanet['name'])


character_list = []
numbers1 = [1,2,3,4,8,14,16,18,19,20,24,25,26,30,33,34,35,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
for x in numbers1:
    character = url + "people/" + str(x)
    testCharacterresponse = requests.get(character)
    testCharacter = testCharacterresponse.json()
    character_list.append(testCharacter['name'])


user_input = input("What's better pizza or tacos?")
if user_input.upper() == "TACOS":
    user_value = 1
else:
    user_value = 2

user_input = input("Do you like summer or winter?")
if user_input.upper() == "WINTER":
    user_value = user_value +1
else:
    user_value = user_value+2

user_input = input("Would you consider yourself on the light or dark side of the force?")
if user_input.upper() == "LIGHT":
    user_value = user_value +2
else:
    user_value = user_value+2

user_input = input("Are you a fan of tea or coffee?")
if user_input.upper() == "COFFEE":
    user_value = user_value +2
else:
    user_value = user_value+2


user_input = input("Have you seen the movie chef? (Yes or No)")
if user_input.upper() == "YES":
    user_value = user_value +3
else:
    user_value = user_value+2

user_input = input("Do you like Star Wars? (Yes or No)")
if user_input.upper() == "NO":
    user_value = 11

# adding a way to have an output in the case that the the number is too high
if user_value >= 11:
    print("Your character is Salacious B. Crumb")
    print("Your vehicle is a Solar Sailer")
    print("Your home planet is Malachor")
else:
    
    print(user_value)
    print(f'Your character is ', character_list[user_value])
    print(f'Your vechicle is ', vehicle_list[user_value*2])
    print(f'Your home planet is ', planet_list[user_value*2])


if __name__ == "__main__":
    application.run(port=5000, debug=True)