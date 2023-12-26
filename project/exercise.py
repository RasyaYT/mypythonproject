# # # Input Exercise
# # input_many = input("How many times do i have to tell you? ")
# # int_many = int(input_many)
# # for char in range(int_many):
# #   print("Clean Up You Room")

# # # For Loop Exercise
# # for number in range(1, 21):
# #   if number == 4 or number == 13:
# #     print(F"{number} is unlucky.")
# #   elif number % 2 == 0:
# #      print(f"{number} is an even number.")
# #   else:
# #      print(f"{number} is an odd number.")
     
# # # While Loop Exercise
# # num = 1
# # while num <= 11:
# #   print(f"the number is {num}")
# #   num += 1

# # for char in range(1, 11):
# #   print("\U0001f600" * char)
# # times = 1
# # while times <= 10:
# #   print("\U0001f600" * times)
# #   times += 1

# # # Loop Exercise
# # user = input("")
# # friend = input("")
# # while not user == friend:
# #   user = input("")
# #   friend = input("")
# # while user == friend:
# #   copying = print("Stop Copying me")
# #   break
# # print("alright you win")

# # # Guess Game
# # import random
# # r_number = random.randint(1, 10)
# # print(r_number)
# # int_guees = None
# # while  int_guees != r_number:
# #   int_guees = input("Guess The Number Between 1 and 10: ")
# #   int_guees = int(int_guees)
# #   if int_guees < r_number:
# #     print("Too low, try again!")
# #   elif int_guees > r_number:
# #     print("Too high, try again!")
# #   else:
# #     print("You guessed it!")
# #   break

# # #LIST EXERCISE
# # list = [1, 2, 3, 4, 5,]
# # i = 0
# # while i < len(list):
# #   print(list[i])
# #   i += 1

# # # Using list comprehensions(the more Pythonic way): 
# # answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
# # #the slice [::-1] is a quick way to reverse a string
# # answer3 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
# # print(answer3)

# # # Without list comprehensions, things are a bit longer:
# # answer2 = []
# # for name in ["Elie", "Tim", "Matt"]:
# #     answer2.append(name[::-1].lower())
# # print(answer2)

# # # Using list comprehensions:

# # answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
# # answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
# # # Using good old manual loops:
# # print(answer2)

# # answer = []
# # for person in ["Elie", "Tim", "Matt"]:
# #     answer.append(person[0])
# # answer2 = []
# # for num in [1,2,3,4,5,6]:
# #     if num % 2 == 0:
# #         answer2.append(num)

# # # Using a string (preferable solution):
# # answer = [char for char in "amazing" if char not in "aeiou"] 
# # print(answer)

# # # Using a list:
# # answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]] 

# # # Nested List
# # answer = [[i for i in range(0,3)] for num in range(0,3)] 
# # print(answer)

# # # To generate the following using a nested list comprehension:

# # [
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #  ]
# # # My solution looks like this:

# # answer = [[i for i in range(0,10)] for num in range(0,10)] 


# # Dictionary
# x = dict(name = "John", age = 36, country = "Norway")

# for v in x.values():
#   print(v)

# for k in x.keys():
#   print(k)
  
# for k,v in x.items():
#   print(f"My {k} is {v}")
  
# # Loop over donations, add all the VALUES together and store in a variable called total_donations

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# total_donations = 0

# for donation in donations.values():
#  total_donations += donation

# # Advanced Version 1 - 
# # This solution uses a built-in function called sum() which I cover in the "Lambdas and Built-In Functions" section.   We haven't talked about how it works, but if you're curious...

# total_donations = sum(donation for donation in donations.values())

# # Advanced Version 2
# # An even better solution using the same sum built-in function is just this nice little line:

# sum(donations.values())

# # Bakery Dictionary Exercise Solution
# # REMEMBER, WE HAVE TO USE FORMAT() RATHER THAN F-STRINGS IN THE UDEMY CODE EDITOR!

# # The following code is common to all solutions:

# # This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# # Solution using IN
# # In the last video, we saw how to use in to test if a value is contained in a dictionary:

# if food in bakery_stock:
#     print("{} left".format(bakery_stock[food]))
# else:
#     print("We don't make that")
# # Solution using get()
# # We can do the same thing using get() and storing the result to a variable.  The variable will either contain the corresponding value from the dictionary OR None.  We can write a simple conditional check:

# quantity = bakery_stock.get(food)
# if quantity:
#     print("{} left".format(quantity))
# else:
#     print("we don't make that")

# My playlIST MUSIC

# playlist = dict(
#   song = "History",
#   author = "Rich Brian",
#   album = "Head in the Clouds"
#   )
# for k,v in playlist.items():
#   print(k,v)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# answer = {list1[i]: list2[i] for i in range(0,3)}
# print(answer)

# for w in range(0, 10):
#     print("*" * 10)

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {k[0]: k[1] for k in person}
# print(answer)

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {k:v for k,v in person}

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = dict(person)
# answer = {count: chr(count) for count in range(65,91)} 
# print(answer)

# s = {1, 4, 5, 4, 5}
# print(s)

# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)

# 3 - Given the following variable:
values = [10,20,30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)

# 3 - Given the following variable
stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)
