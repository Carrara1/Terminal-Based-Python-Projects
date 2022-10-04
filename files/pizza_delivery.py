print("Welcome to Goofy ahh's pizza delivery! ")
size = input("What size do you want? Options: S, M or L. ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

size_s = size == "S"
size_m = size == "M"
size_l = size == "L"

if size_s:
    bill += 15
elif size_m:
     bill += 20
elif size_l:
    bill += 25
else:
    print("Thats the wrong option bro. Try again. ")

if add_pepperoni == "Y":
    if size_s: 
        bill += 2
    else: 
        bill += 3

if extra_cheese == "Y":
    if size_s: 
        bill += 1
    else: 
        bill += 2

print(f"Your pizza will be ${bill} Dollars.")

