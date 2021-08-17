import random
print("number Guessing Game")
number = random.randint(1,9)
chanses = 0
print("guess a number(between 1 and 9): ")
while chanses < 5:
    guess = int(input("Enter Your guess:-"))
    
    if guess == number:
        print("Congractulations you won")
        break
    elif guess < number:
        print("Your guess was too low: Guess a number heigher than",guess)
    else:
        print("Your guess was too heigh: Guess a number lower than",guess)
    chanses += 1
if not chanses < 5:
    print("You lose and the number is:",number)