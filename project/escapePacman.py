# Start Coding

print('''================================================.
     .-.   .-.     .--.                         |
    | OO| | OO|   / _.-' .-.   .-.  .-.   .''.  |
    |   | |   |   \  '-. '-'   '-'  '-'   '..'  |
    '^^^' '^^^'    '--'                         |
===============.  .-.  .================.  .-.  |
               | |   | |                |  '-'  |
               | |   | |                |       |
               | ':-:' |                |  .-.  |
l42            |  '-'  |                |  '-'  |
==============='       '================'       |''')

print('escape the pacman')
firstChoice = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".')


if firstChoice == "right":
    secondChoice = input('You\'ve come to a right side. Type "wait" or "explore".').lower()
    if secondChoice == "wait":
        thirdChoice = input('you arrive at the escape door. There is 3 doors. One Red, one yellow and one blue. Which colour do you choose?').lower()
        if thirdChoice == "red":
            print("its room full fire. Game Over")
        elif thirdChoice == "yellow":
            print("You escape the pacman! You Win!")
        elif thirdChoice == "blue":
            print("You enter a room of pacman. Game Over")
        else:
            print("You choose a door that doesn't exist. Game Over")
    else:
        print('You get attacked by an angry pacman. Game Over')
else:
    print('You get caught by pacman. Game Over')