print("WELCOME TO BMI CALCULATOR")
weight = float(input("What is your weight :"))
height = float(input("What is your height :"))

BMI = weight / (height ** 2)
print(f"Your BMI is {BMI}")
if BMI < 18.5:
    print("Underweight")
elif BMI == 18.5 or BMI < 25:
    print("Normal Weight")
elif BMI >= 25:
    print("Over Weight")

