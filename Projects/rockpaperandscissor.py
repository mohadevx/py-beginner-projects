# code by @moiibrahem
# The fisrt project in this repo

import random as rd

# the rules of the game
rules = ["rock", "paper", "scissor"]
a = rules[0]
b = rules[1]
c = rules[2]

# the choices that computer generating
computer = rd.choice(rules)
# the results will show after choose
result = ["YOU WIN", "YOU LOSE", "DRAW"]

print('''---THE RULES---
1. Write in small alphabets
2. Your choices [rocks, paper, scissor]
3. That's it!
''')


# your choice
choice = input("Write your choice: ")

# game gui haha jk :)
if choice != rules:
    print("You: " + choice)
    print("Computer: " + computer)

# the final result
if choice == a and computer == c:
    print("The result: " + result[0])
elif choice == computer:
    print("The result: " + result[2])
elif choice == b and computer == a:
    print("The result: " + result[0])
elif choice == c and computer == b:
    print("The result: " + result[0])
elif choice == a and computer == b:
    print("The result: " + result[1])
elif choice == b and computer == c:
    print("The result: " + result[1])
elif choice == c and computer == a:
    print("The result: " + result[1])
# spelling mistakes maybe
else:
    print("Wrong input! check THE RULES, please.")