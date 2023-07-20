
# F String
age = input("What is you current age?")

intAge = int(age)

yearsRemaining = 90 - intAge;
daysRemaining = yearsRemaining * 365;
weeksRemaining = yearsRemaining * 52;
monthsRemaining = yearsRemaining * 12;

print(f"you have {daysRemaining} days, {weeksRemaining} weeks, and {monthsRemaining} months left.")