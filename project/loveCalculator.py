
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combineString = name1 + name2
lowerName = combineString.lower()

t = lowerName.count('t')
r = lowerName.count('r')
u = lowerName.count('u')
e = lowerName.count('e')

true = t + r + u + e

l = lowerName.count('l')
o = lowerName.count('o')
v = lowerName.count('v')
e = lowerName.count('e')



love = l + o + v + e

loveScore = int(str(true) + str(love))

print(loveScore)

if (loveScore < 10) or (loveScore > 90):
  print(f"Your score is {loveScore}, you go together like coke andmentos.")
elif (loveScore >= 40) or (loveScore <= 50):
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"your score is {loveScore}")