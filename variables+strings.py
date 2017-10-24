# -*- coding: utf-8 -*-
# variables+strings.py

'''
This is a beginner Python tutorial that shows how to use variables with 
strings of text. First I will show ways to print messages that use variables
alongside strings to complete messages. Then I will show how we can embed
variables in strings using "format"
'''

# First, let's create our variables!

year = 2017
month = "October"
day = 23

# Printing variables alongside strings
# Notice the printed copy is broken between strings and variables
# We partition this different information using commas.
print("Today is", month, day, ",", year, "and I am finally learning Python!")

# Embedding variables within strings
# Notice the f before the first double quote - this is what allows embedding
# of variables!
print(f"Today is {month} {day}, {year} and I am finally learning Python!")
