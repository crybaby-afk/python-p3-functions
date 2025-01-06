#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    # pass

def greet(name):
    print("Hello, " + name+"!")
greet("larry")

def greet_with_default(name="programmer"):
    print("Hello, " + name +"!") 
greet_with_default("Larry")

def add(num1, num2):
    return(num1 + num2)
print(add(2,4))
    # pass

def halve(number):
    return(number/2)
print(halve(88))
    
