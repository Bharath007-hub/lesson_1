height = float(input("enter your height in cm"))
weight = float(input("enter your weight in kg"))

bmi = weight / (height/100)**2

print("your BMI is: ", bmi)

if bmi <= 18.4:
    print("your under weight")

elif bmi <= 24.9:
    print("you are healthy")

elif bmi <= 29.9:
    print("you are over weight")

elif bmi <= 34.9:
    print("you are severly over weight")

elif bmi <= 39.9:
    print("you are obese.")

else:
    print("error")