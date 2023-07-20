# if the bill is 150.00, split between 5 people, with 12% tip
# each person should pay (150.00 / 5) * 1.12

print("Welcome To The Tip Calculator")
totalBill = float(input("What Was The Total Bill? $"))
tip = int(input("What Percentage tip  would you like to give? 10, 12, or 15?"))
splitBill = int(input("How many people to split the bill?"))


tipPercent = tip / 100
totalTip = totalBill * tipPercent
total_Bill = totalBill + totalTip
billPerson = totalBill / splitBill
final = round(billPerson, 2)
shouldPay = print(f"Each person should pay: ${final}")

