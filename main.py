# Tip Calculator Project

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give?")
no_of_people = input("How many people to split the bill?")
per_person_pay = (float(total_bill) / int(no_of_people)) * (1.00 + int(percentage_tip) / 100)
final_amount = round(per_person_pay, 2)
print(f"Each person should pay ${final_amount}.")
