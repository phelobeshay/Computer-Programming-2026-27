#Phelopatir Beshay
# Computer Programming, period 4
# Assignment: Project 1 (Z's System)
# 30 September 2026

#Menu Items (no tax)
burrito_basePrice = 4.5
burger_basePrice = 4
hotdog_basePrice = 3
teriyaki_basePrice = 5
#Menu Items (taxable)
chips_basePrice = 1
chips_taxPrice = 1.1
fries_basePrice = 2.5
fries_taxPrice = 2.75
soda_basePrice = 1.75
soda_taxPrice = 1.93
water_basePrice = 1.5
water_taxPrice = 1.65

#Variables for ordering
total_noTax = 0
total_tax = 0
item1 = input("What would you like to order first? ")
quantity1 = int(input("How many would you like to order? "))
item2 = input("What would you like to order second? ")
quantity2 = int(input("How many would you like to order? "))
item3 = input("What would you like to order third? ")
quantity3 = int(input("How many would you like to order? "))
item4 = input("What would you like to order last? ")
quantity4 = int(input("How many would you like to order? "))
total_quantity = quantity1 + quantity2 + quantity3 + quantity4

#Item 1 Detection (no tax)
if item1.lower() == "breakfast burrito":
    item1_basePrice = burrito_basePrice
    item1_totalPrice = item1_basePrice * quantity1
    total_noTax = total_noTax + item1_totalPrice
    total_tax = total_tax + item1_totalPrice
if item1.lower() == "cheeseburger":
    item1_basePrice = burger_basePrice
    item1_totalPrice = item1_basePrice * quantity1
    total_noTax = total_noTax + item1_totalPrice
    total_tax = total_tax + item1_totalPrice
if item1.lower() == "hot dog" or item1.lower() == "hotdog":
    item1_basePrice = hotdog_basePrice
    item1_totalPrice = item1_basePrice * quantity1
    total_noTax = total_noTax + item1_totalPrice
    total_tax = total_tax + item1_totalPrice
if item1.lower() == "teriyaki bowl":
    item1_basePrice = teriyaki_basePrice
    item1_totalPrice = item1_basePrice * quantity1
    total_noTax = total_noTax + item1_totalPrice
    total_tax = total_tax + item1_totalPrice

#Item 1 Detection (tax)
if item1.lower() == "chips":
    item1_basePrice = chips_basePrice
    item1_taxPrice = chips_taxPrice
    item1_totalPrice = item1_basePrice * quantity1
    total_noTax = total_noTax + item1_totalPrice
    total_tax = total_tax + (item1_taxPrice * quantity1)
if item1.lower() == "fries":
    item1_basePrice = fries_basePrice
    item1_taxPrice = fries_taxPrice
    item1_totalPrice = item1_basePrice * quantity1
    total_noTax = total_noTax + item1_totalPrice
    total_tax = total_tax + (item1_taxPrice * quantity1)
if item1.lower() == "soda":
    item1_basePrice = soda_basePrice
    item1_taxPrice = soda_taxPrice
    item1_totalPrice = item1_basePrice * quantity1
    total_noTax = total_noTax + item1_totalPrice
    total_tax = total_tax + (item1_taxPrice * quantity1)
if item1.lower() == "water":
    item1_basePrice = water_basePrice
    item1_taxPrice = water_taxPrice
    item1_totalPrice = item1_basePrice * quantity1
    total_noTax = total_noTax + item1_totalPrice
    total_tax = total_tax + (item1_taxPrice * quantity1)




#Item 2 Detection (no tax)
if item2.lower() == "breakfast burrito":
    item2_basePrice = burrito_basePrice
    item2_totalPrice = item2_basePrice * quantity2
    total_noTax = total_noTax + item2_totalPrice
    total_tax = total_tax + item2_totalPrice
if item2.lower() == "cheeseburger":
    item2_basePrice = burger_basePrice
    item2_totalPrice = item2_basePrice * quantity2
    total_noTax = total_noTax + item2_totalPrice
    total_tax = total_tax + item2_totalPrice
if item2.lower() == "hot dog" or item2.lower() == "hotdog":
    item2_basePrice = hotdog_basePrice
    item2_totalPrice = item2_basePrice * quantity2
    total_noTax = total_noTax + item2_totalPrice
    total_tax = total_tax + item2_totalPrice
if item2.lower() == "teriyaki bowl":
    item2_basePrice = teriyaki_basePrice
    item2_totalPrice = item2_basePrice * quantity2
    total_noTax = total_noTax + item2_totalPrice
    total_tax = total_tax + item2_totalPrice

#Item 2 Detection (tax)
if item1.lower() == "chips":
    item2_basePrice = chips_basePrice
    item2_taxPrice = chips_taxPrice
    item2_totalPrice = item2_basePrice * quantity2
    total_noTax = total_noTax + item2_totalPrice
    total_tax = total_tax + (item2_taxPrice * quantity2)
if item2.lower() == "fries":
    item2_basePrice = fries_basePrice
    item2_taxPrice = fries_taxPrice
    item2_totalPrice = item2_basePrice * quantity2
    total_noTax = total_noTax + item2_totalPrice
    total_tax = total_tax + (item2_taxPrice * quantity2)
if item2.lower() == "soda":
    item2_basePrice = soda_basePrice
    item2_taxPrice = soda_taxPrice
    item2_totalPrice = item2_basePrice * quantity2
    total_noTax = total_noTax + item2_totalPrice
    total_tax = total_tax + (item2_taxPrice * quantity2)
if item2.lower() == "water":
    item2_basePrice = water_basePrice
    item2_taxPrice = water_taxPrice
    item2_totalPrice = item2_basePrice * quantity2
    total_noTax = total_noTax + item2_totalPrice
    total_tax = total_tax + (item2_taxPrice * quantity2)




#Item 3 Detection (no tax)
if item3.lower() == "breakfast burrito":
    item3_basePrice = burrito_basePrice
    item3_totalPrice = item3_basePrice * quantity3
    total_noTax = total_noTax + item3_totalPrice
    total_tax = total_tax + item3_totalPrice
if item3.lower() == "cheeseburger":
    item3_basePrice = burger_basePrice
    item3_totalPrice = item3_basePrice * quantity3
    total_noTax = total_noTax + item3_totalPrice
    total_tax = total_tax + item3_totalPrice
if item3.lower() == "hot dog" or item3.lower() == "hotdog":
    item3_basePrice = hotdog_basePrice
    item3_totalPrice = item3_basePrice * quantity3
    total_noTax = total_noTax + item3_totalPrice
    total_tax = total_tax + item3_totalPrice
if item3.lower() == "teriyaki bowl":
    item3_basePrice = teriyaki_basePrice
    item3_totalPrice = item3_basePrice * quantity3
    total_noTax = total_noTax + item3_totalPrice
    total_tax = total_tax + item3_totalPrice

#Item 3 Detection (tax)
if item3.lower() == "chips":
    item3_basePrice = chips_basePrice
    item3_taxPrice = chips_taxPrice
    item3_totalPrice = item3_basePrice * quantity3
    total_noTax = total_noTax + item3_totalPrice
    total_tax = total_tax + (item3_taxPrice * quantity3)
if item3.lower() == "fries":
    item3_basePrice = fries_basePrice
    item3_taxPrice = fries_taxPrice
    item3_totalPrice = item3_basePrice * quantity3
    total_noTax = total_noTax + item3_totalPrice
    total_tax = total_tax + (item3_taxPrice * quantity3)
if item3.lower() == "soda":
    item3_basePrice = soda_basePrice
    item3_taxPrice = soda_taxPrice
    item3_totalPrice = item3_basePrice * quantity3
    total_noTax = total_noTax + item3_totalPrice
    total_tax = total_tax + (item3_taxPrice * quantity3)
if item3.lower() == "water":
    item3_basePrice = water_basePrice
    item3_taxPrice = water_taxPrice
    item3_totalPrice = item3_basePrice * quantity3
    total_noTax = total_noTax + item3_totalPrice
    total_tax = total_tax + (item3_taxPrice * quantity3)




#Item 4 Detection (no tax)
if item4.lower() == "breakfast burrito":
    item4_basePrice = burrito_basePrice
    item4_totalPrice = item4_basePrice * quantity4
    total_noTax = total_noTax + item4_totalPrice
    total_noTax = total_tax + item4_totalPrice
if item4.lower() == "cheeseburger":
    item4_basePrice = burger_basePrice
    item4_totalPrice = item4_basePrice * quantity4
    total_noTax = total_noTax + item4_totalPrice
    total_noTax = total_tax + item4_totalPrice
if item4.lower() == "hot dog" or item4.lower() == "hotdog":
    item4_basePrice = hotdog_basePrice
    item4_totalPrice = item4_basePrice * quantity4
    total_noTax = total_noTax + item4_totalPrice
    total_noTax = total_tax + item4_totalPrice
if item4.lower() == "teriyaki bowl":
    item4_basePrice = teriyaki_basePrice
    item4_totalPrice = item4_basePrice * quantity4
    total_noTax = total_noTax + item4_totalPrice
    total_noTax = total_tax + item4_totalPrice

#Item 4 Detection (tax)
if item4.lower() == "chips":
    item4_basePrice = chips_basePrice
    item4_taxPrice = chips_taxPrice
    item4_totalPrice = item4_basePrice * quantity4
    total_noTax = total_noTax + item4_totalPrice
    total_tax = total_tax + (item4_taxPrice * quantity4)
if item4.lower() == "fries":
    item4_basePrice = fries_basePrice
    item4_taxPrice = fries_taxPrice
    item4_totalPrice = item4_basePrice * quantity4
    total_noTax = total_noTax + item4_totalPrice
    total_tax = total_tax + (item4_taxPrice * quantity4)
if item4.lower() == "soda":
    item4_basePrice = soda_basePrice
    item4_taxPrice = soda_taxPrice
    item4_totalPrice = item4_basePrice * quantity4
    total_noTax = total_noTax + item4_totalPrice
    total_tax = total_tax + (item4_taxPrice * quantity4)
if item4.lower() == "water":
    item4_basePrice = water_basePrice
    item4_taxPrice = water_taxPrice
    item4_totalPrice = item4_basePrice * quantity4
    total_noTax = total_noTax + item4_totalPrice
    total_tax = total_tax + (item4_taxPrice * quantity4)




#Once order is complete
line1 = "Item\tQuantity\tBase Amount\t Total Amount"
line3 = f"{item1.title()}\t{quantity1}\t${item1_basePrice}\t${item1_totalPrice}"
line4 = f"{item2.title()}\t{quantity2}\t${item2_basePrice}\t${item2_totalPrice}"
line5 = f"{item3.title()}\t{quantity3}\t${item3_basePrice}\t${item3_totalPrice}"
line6 = f"{item4.title()}\t{quantity4}\t${item4_basePrice}\t${item4_totalPrice}"
line8 = f"TOTAL\t{total_quantity}\t${total_noTax}\t${total_tax}"

print(line1)
print("--------------------------------------------------")
print(line3)
print(line4)
print(line5)
print(line6)
print("--------------------------------------------------")
print(line8)

#Payment
cubcash_balance = 100
payment_cash = False

payment = input("How would you like to pay? (Cash/Cub Cash) ")
if payment.lower() == "cash":
    payment_cash = True
elif payment.lower() == "cub cash":
    payment_cash = False

if payment_cash == True:
    amount_given = int(input("How much will you give to the cashier? "))
    change = amount_given - total_tax
    if change < 0:
        print(f"{change * -1} left to pay.")
        amount_given = int(input("Please give more cash to complete your order. "))
        change = amount_given - (change * -1)
    elif change == 0:
        print("Thank you for shopping at Z's. Have a good day!")
    elif change > 0:
        print(f"Your change is ${change}.\nThank you for shopping at Z's. Have a good day!")
elif payment_cash == False:
    cubcash_balance = cubcash_balance - total_tax
    if cubcash_balance < 0:
        print("Card declined.")
    else:
        print(f"Remaining balance is ${cubcash_balance}.\nThank you for using Cub Cash. Have a good day!")