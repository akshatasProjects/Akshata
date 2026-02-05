print("WELCOME TO TIP CALCULATOR ")
bill = float(input("What was the total bill? :"))
tip = int(input("What is the % tip would you like to give? 10 12 15: "))
people = int(input("How many people to split the bill?: "))

calc_perc = tip / 100
print(f"Percent is {calc_perc}")
bill = (bill * calc_perc)+bill
print(f"Calculated bill:{bill}")
div = bill / people
print(round(div, 2))