import random
print("number guessing game")
number=random.randint(1,9)
chances=0
print("GUESS THE NUMBER(between 1 and 9)")
while chances <5:
    guess=int(input("ENTER YOUR GUESS"))
    if guess==number:
        print("CONGRATULATIONS YOU WON")
        break
    elif guess < number:
        print("YOUR GUESS WAS TOO LOW",guess)
    else:
        print("YOUR GUESS WAS TOO HIGH:guess a number lower than this",guess)
    chance+=1
if not chances <5:
 print("YOU LOOSE! THE NUMBER IS, NUMBER")