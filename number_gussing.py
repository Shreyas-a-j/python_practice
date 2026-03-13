import random

def top_range_fn():
    top_range = input("Type a number: ")
    if top_range.isdigit():
        t_range = int(top_range)
        return t_range
    else:
        print("Please enter a number: ")
        return top_range_fn()

random_number = random.randint(1,top_range_fn())

def guess_number(value, number_guess):
    number_guess += 1
    if value > random_number:
        print("High!")
    elif value < random_number:
        print("Low!")
    elif value == random_number:
        print("Correct :) ")
        print("Total Guesses: " + str(number_guess))
        quit()
    return guess_number(int(input("Guess again: ")),int(number_guess))

guess_number(int(input("Guess the number: ")),0)