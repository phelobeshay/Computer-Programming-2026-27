# Beshay, Phelopatir
# Computer Programming, period 4
# Assignment: Homework 5
# 15 September 2026

altitude_log = [0, 134, 294, 392, 583, 605, 896, 1059]
print(f"Flight log has been created: {altitude_log}")
#Created the variable "altitude_log" with 8 values
altitude_log.append(1123)
altitude_log.append(1344)
print(f"Two new readings have been added: {altitude_log}")
#Appended two new values: 1,123 and 1,344
altitude_log.pop(0)
altitude_log.pop(0)
print(f"The first and second reading are corrupted. They have been removed: {altitude_log}")
#Popped the values 0 and 134
altitude_log.insert(2, 439)
print(f"A dropped reading, {altitude_log[2]}, has been discovered and reintroduced.")
print(f"Final flight log: {altitude_log}")
#Inserted value 439 at index 2