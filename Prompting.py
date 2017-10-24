# -*- coding: utf-8 -*-
# "Prompting The User with Input"

# This beginner Python exercise uses prompts to elicit and store info
# from the user. At the end it prints a statement containing all of the
# information collected from the user.

# This asks the user for their name upon script launch
user_name = input("What is your name?")
# This formats subsequent prompts with a nice little chevron :)
prompt = '> '

# Note the "f" before the first double quote. This formats the string
# so that it accommodates embedded variables.
print(f"Hi {user_name}, I'm a prompt script.")
print("I'd like to ask you a few questions.")

# Our first prompt! Asks how long user has been studying Python.
print(f"How long have you been learning Python?")
PyLearn = input(prompt)

# Second prompt asks user to share what city they live in.
print(f"What city do you live in, {user_name}?")
lives = input(prompt)

# Third prompt asks user to share the name of their favorite internet browser.
print("What is your favorite Internet browser?")
browser = input(prompt)

# Alright, wrapping it all up below!
print(f"""
Alright, so you said you have been learning Python for {PyLearn}.
You're doing great! In addition you mentioned you live in {lives}. 
I've never been there, but it sounds like a cool place!.
Also - your favorite Internet browser is {browser}?!
No way - {browser} is my favorite, too!
""")
