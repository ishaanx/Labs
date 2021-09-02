## Lab 101

# Generate triangle
def tri(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
n=5
tri(n)

# Print int, float, string
def types():
    x=5.555
    print(int(x))
    print(float(x))
    print(str(x))
types()

# Print List
def list():
    mylist= ["apple","orange"]
    print(mylist)
list()

# Print Tuple
def tuple():
    mytuple=("apple","bananas")
    print(mytuple)
tuple()

## Create a program that asks the user to enter 
## their name and their age. Print out a message 
## addressed to them that tells them the year that 
## they will turn 100 years old.
import datetime as dt
from random import randint
def userprint():
        print("Enter your name: ")
        myname=input()
        print("Enter your age: ")
        myage=input()
        myear=2050
        current_year = dt.date.today().year
        age_calc = int(current_year) - int(myage)
        hundred_year = age_calc + 100
        print("Hi " + myname + ", you will turn 100 years old in the year "+ str(hundred_year))
userprint()

## Ask the user for a number. Depending on 
## whether the number is even or odd, print out an 
## appropriate message to the user.
def evenodd():
    x = int(input("Enter a number: "))
    if (x%2)==0:
        print("Number is even")
    else:
        print("Number is odd")
evenodd()

## Write a program that accepts a sentence and calculate the number of letters and digits.
def counting():
    total_numbers = 0
    total_strings = 0
    string = str(input("Enter any string: "))
    for s in string:
        if s.isnumeric():
            total_numbers += 1
        else:
            total_strings += 1
    print("Total letters found: ",total_strings)
    print("Total digits found: ",total_numbers)
counting()

## Define a function which can compute the sum of two numbers.
def sum():
    a= int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b
    print("The sum is: ", c)
sum()


## Create a 8 character alphanumeric string random password generator.
def paswd():
    import random
    pass_data = "qwertyuiopasdfgjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890[];',./!@#$%^&*()_+:<>?"
    password = "".join(random.sample(pass_data, 8))
    print(password)
paswd()


## Write a function to compute 5/0 and use try/except to catch the exceptions.
def five():
    try:
        x = 5/0
    except ZeroDivisionError:
        print("Cannot divide by zero")
five()

## Generate a random number between 1 and 9 
## (including 1 and 9). Ask the user to guess the 
## number, then tell them whether they guessed 
## too low, too high, or exactly right. 
def random_gen():
    import random
    userNumber = int(input("Enter any number: "))
    randomNumber = randint(1,9)
    if userNumber == randomNumber:
        print("You guessed the exact number!")
    elif userNumber < randomNumber:
        print("You guessed too low")
    else:
        print("You guessed too high")
random_gen()
##