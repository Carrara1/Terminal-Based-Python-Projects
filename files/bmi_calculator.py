
height = float(input("enter ur height: "))
weight = float(input("enter ur weight: "))

bmi = (weight / height ** 2) 

print(f"your bmi is {bmi} ")

if bmi > 35:
    print("You are clinically obese! ")
elif bmi > 30 < 35:
    print("You are obese! ")
elif bmi > 25 < 30:
    print("You are overweight. ")
elif bmi > 18.5 < 25:
    print("You have a normal weight. ")
else: 
    print("You are underweight. ")  

  
  


