## Lab 101

def tri(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
n=5
#tri(n)
#
#x=5.555
#print(int(x))
#print(float(x))
#print(str(x))
#
#mylist= ["apple","orange"]
#print(mylist)
#
#mytuple=("apple","bananas")
#print(mytuple)

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
#userprint()

def evenodd():
    x = int(input("Enter a number: "))
    if (x%2)==0:
        print("Number is even")
    else:
        print("Number is odd")
#evenodd()

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
#counting()

def sum():
    a= int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b
    print("The sum is: ", c)
#sum()


def paswd():
    import random
    pass_data = "qwertyuiopasdfgjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890[];',./!@#$%^&*()_+:<>?"
    password = "".join(random.sample(pass_data, 8))
    print(password)


def five():
    try:
        x = 5/0
    except ZeroDivisionError:
        print("Cannot divide by zero")
#five()

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