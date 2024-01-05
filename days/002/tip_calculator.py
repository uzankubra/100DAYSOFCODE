print("Welcome to tip calculator.")
total_bill = input("What's the total bill?")
total_people = input("How many people to split the bill?")
percentage = input("What percentage tip would you like to give? 10,12 or 15")

each_person_pay = float(
    (int(total_bill) / int(total_people)) * (int(percentage) / 100))
print("Each person should pay:" + str(each_person_pay))
