
import random
"""Multiplication table
    input = integer (num)
    output = num's table until num * 10"""

num = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{num} * {i} = {num * i}")

""" sum 1-100
    input: 1-100 nums
    output: sum of 1-100 in an accumulator"""
#method 1
acc = 0
for i in range(1,101):
    acc += i
print(f"\nThe total sum is {acc}")

#method 2
n = 100
sum = n * (n +1) // 2
print(f"The sum is {sum}")

"""Fizz/Buzz/FizzBuzz
    input: 1-50 nums Output: if num divided by both 3&5 then FizzBuzz, 
    if only divided by 3 then Fizz, if only by 5 then Buzz, else the number as it is."""

print("\nFizzBuzz :")
for i in range(1,51):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)

"""Number guessing game:
    input: int values (guesses)
    output: if guess doesn't match- try again | 
    if guess is right then guessed correctly"""

number = random.randint(1,100)
guess = int(input("\nGuess the number: "))

while(guess != number):
    diff = "Higher" if guess < number else "Lower"
    guess = int(input(f"Wrong guess try {diff}:"))
if(guess == number):
    print("You guessed it right !!")

