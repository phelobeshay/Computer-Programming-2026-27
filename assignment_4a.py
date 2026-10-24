# Beshay, Phelopatir
# Computer Programming, period 4
# Assignment: Homework 4a
# 23 October 2026

#Part A
#Question A
info_dad = {
    "First Name":"Atef",
    "Last Name":"Beshay",
    "Age":50,
    "City":"Santa Monica"
}
for k,v in info_dad.items():
    print(k,":",v)
#Question B
aboutme = {
    "name":"Phelopatir Beshay",
    "age":16,
    "favFood":["fries", "burgers", "pancakes", "fried chicken"],
    "hairColor":"black",
    "favSubject":"math",
    "favSweet":"chocolate",
    "favHobbies":["video games", "swimming", "coding", "sleeping"],
    "likeCoding":True
}
print(aboutme)
#Question C
phonebook = {
    "John":938477566,
    "Jack":938377264,
    "Jill":947662781
}
phonebook["Jake"] = 938273443
phonebook.pop("Jill")

#Part B
#Question 1/2
glossary = {
    "eschew":"to avoid",
    "germane":"relevant",
    "arrogate":"to take without right",
    "congeal":"to thicken",
    "banal":"commonplace",
    "celerity":"swiftness",
    "avid":"intensely eager",
    "brackish":"having a salty taste and unpleasant to drink",
    "accost":"to approach and speak to first",
    "myopic":"nearsighted"
}
for k, v in glossary.items():
    print(f"{k.title()} - {v}\n")
#Question 3
rivers = {
    "nile":"egypt",
    "mississippi":"the united states",
    "rio grande":"mexico"
}
for k,v in rivers.items():
    print(f"The {k.title()} is a river located in {v.title()}.")
for k,v in rivers.items():
    print(k.title())
    print(v.title())
#Question 4
people = {
    "person1":{
        "firstName":"John",
        "lastName":"Beshay",
        "favColor":"green",
        "birthMonth":"july"
    },
    "person2":{
        "firstName":"Atef",
        "lastName":"Beshay",
        "favColor":"red",
        "birthMonth":"july"
    },
    "person3":{
        "firstName":"Jacqueline",
        "lastName":"Habishi",
        "favColor":"purple",
        "birthMonth":"june"
    }
}
for k in people.items():
    print(k)
#Question 5
cities ={
    "los angeles":{
        "country":"united states",
        "population":"3.87 million",
        "fact":"most populated city in california"
    },
    "cairo":{
        "country":"egypt",
        "population":"9.8 million",
        "fact":"its often referred to as egypt in arabic"
    },
    "oaxaca":{
        "country":"mexico",
        "population":"258 thousand",
        "fact":"largest number of indigenous people in mexico"
    }
}
print(cities)