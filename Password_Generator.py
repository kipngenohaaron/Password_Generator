#!/usr/bin/python

import random

# Introduction
print('Welcome to our Password Generator App!')
print("\n")

# User input: preferred characters, number of passwords, and password length
characters = input('Enter your preferred characters to make a password: ')
num_passwords = int(input('How many passwords would you like to be generated: '))
lengthPasswords = int(input('Enter th#!/usr/bin/python

import random

# Introduction
print('Welcome to our password generator app!')
print("\n")

# User input: preferred characters, number of passwords, and password length
characters = input('Enter your preferred characters to make a password: ')
num_passwords = int(input('How many passwords would you like to be generated: '))
lengthPasswords = int(input('Enter the length of the password you would wish to have: '))
print('Here are your passwords: ')

# Generate and display the passwords
for pwd in range(num_passwords):
    password = ''
    for c in range(lengthPasswords):
        password += random.choice(characters)
    print(password)
e length of the password you would wish to have: '))
print('Here are your passwords: ')

# Generate and display the passwords
for pwd in range(num_passwords):
    password = ''
    for c in range(lengthPasswords):
        password += random.choice(characters)
    print(password)

    Example
# python Password_Generator.py 
# Welcome to our password generator app!


# Enter your preferred characters to make a password: kipngenohaaron
# How many passwords would you like to be generated: 5
# Enter the length of the password you would wish to have: 6
# Here are your passwords: 
# enpnek
# kehhai
# roapni
# nhagok
# pnnrgk
