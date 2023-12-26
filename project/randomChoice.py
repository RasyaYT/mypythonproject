import random

test_seed = int(input('Create a sedd number: '))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

randomChoice = random.choice(names)
finalChoice = f"{randomChoice} is going to buy the meal today!"

print(finalChoice)
