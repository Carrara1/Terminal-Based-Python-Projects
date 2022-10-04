 
print("Welcome to the tip calculator! ")

total_bill = float(input("What was the total bill? $"))

tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

num_ppl = int(input("How many people to split the bill? "))

divide_value = (total_bill * (1+ tip_percent/100))/num_ppl

print(f"Each person should pay: ${round(divide_value, 2)}")