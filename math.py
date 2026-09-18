import random
import math

print("Welcome to Random Fun Calculator!")

lucky_number = random.randint(1, 100)
print("Your lucky number is:", lucky_number)

activities = ["Watch a movie", "Play a game", "Read a book", "Go for a walk", "Listen to music"]
activity = random.choice(activities)
print("Your random activity is:", activity)

print("\nNumber Guessing Game")

number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number from 1 to 10: "))

    if guess == number:
        print("You guessed it!")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

print("\nMath Module Functions")

num = 5.7
num2 = 2.3

print("Ceil of", num, ":", math.ceil(num))
print("Floor of", num, ":", math.floor(num))
print("Copysign:", math.copysign(num, -1))
print("Absolute value:", math.fabs(-10.5))
print("GCD of 24 and 36:", math.gcd(24, 36))

print("\nThank you for using Random Fun Calculator!")