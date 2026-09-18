# Beshay, Phelopatir
# Computer Programming, period 4
# Assignment: Homework 3
# 15 September 2026

#Part 1
hobbies = ["video games", "swimming", "coding", "speech and debate", "biking"]
print(hobbies)
print(len(hobbies))
print(hobbies[2])
print(hobbies[0])
#Part 2
hello_list = ["hello!"]*100
print(hello_list)
#Part 3
list1 = ["pumpkin", "halloween", "jack-o-lantern", "spooky"]
list2 = ["christmas", "new year", "holiday", "santa"]
list3 = list1 + list2
print(list3)
#Part 4
favFoods=["pancakes", "chocolate chip cookies", "chicken", "cucumbers", "french fries"]
print(len(favFoods))
print(favFoods[2])
print(favFoods[-4])
favFoods.append("Phelo")
favFoods.insert(2, 16)
favFoods.remove("cucumbers")
print(favFoods)
#Part 5
numbers = list(range(1, 21))
for thing in numbers:
    print(thing)
#Part 6
odd_numbers = list(range(1, 20, 2))
for thing in odd_numbers:
    print(thing)
#Part 7
common_animals = ["lion", "tiger", "cheetah"]
for thing in common_animals:
    print(f"A {thing} is a cat.")
print("All of these animals are cats!")
#Part 8/9
dinner_people = ["Jay-Z", "Toby Fox", "Jesus Chirst"]
for people in dinner_people:
    print(f"{people}, you are invited to dinner.")

print(f"{dinner_people[1]} can't make it to dinner.")
dinner_people.pop(1)
dinner_people.insert(1, "Akira Toriyama")
for people in dinner_people:
    print(f"{people}, you are invited to dinner.")