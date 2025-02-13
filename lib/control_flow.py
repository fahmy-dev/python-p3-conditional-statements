#!/usr/bin/env python3

import ipdb

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

admin_login("Admin", "12345")

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):

    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return num


def calculator(operation, num1, num2):
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 
    }
    result = operations.get(operation, None)
    if result is None:
        print("Invalid operation!")
        return None
    return result


calculator("/", 10, 5)