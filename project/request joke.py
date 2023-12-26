import asci
import requests
print(asci.ascii_dad)

ui = input("Let me tell you a joke! Give me a topic:  ")
ui_limit = input("How many jokes you want see?: ")
url = "https://icanhazdadjoke.com/search"
joke = requests.get(url, headers={"accept": "text/plain"},
                    params={"term": ui, "limit": ui_limit,})
r = requests.get(url, headers={
                               "accept": "application/json"},
                                  params={
    "term": ui, "limit": 1,
}
)


data = r.json()
total_jokes = data["total_jokes"]

if total_jokes >= 1:
   print(f"I've got {total_jokes} joke about {ui}. Here it is: ")
print(joke.text)

if total_jokes == 0:
    print(f"Sorry, i don't have any jokes about {ui}! Please try again")

#                  params={
#     "term": ui, "limit": 1,
# }

