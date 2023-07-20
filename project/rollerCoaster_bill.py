# IF ELSE STATEMENT

print("Welcome to the rollercoaster!")
h = int(input('What is you height in cm? '))
a = int(input('What is you age? '))
p =  input('Want take a photo? Y or N ')

if h >= 120:
    print("you can play rollercoaster")
    if a < 12:
        bill = 5
        print("you should pay 5$.")
    elif a <= 18:
        bill = 7
        print("you should pay 7$.")
    elif a < 22:
        bill = 15
        print("you should pay 15$")
    elif a >= 45 or a <= 55 :
        bill = 0
        print("free")
    else:
        bill = 12
        print("you should pay 12$.")
    if p  == "Y":
        bill += 3
        print(f"your final bill is ${bill}")    
else:
    print("you can't play rollercoaster")