# -*- coding: utf-8 -*-
# Multiply 4 Integers
# This is a beginner Python script that allows the user to multiply 4 integers
# while launching the script in terminal. Follow the instructions in the comments below!

from sys import argv

# The module "argv" collects 4 arguments entered with the launch of 
# this Python script

# NOTE In terminal:
#     Launch this file with Python3.6 mult4integers.py num1 num2 num3 num4
#     with integers in place of the "num#" arguments.

script, num1, num2, num3, num4 = argv

# Print the product of the 4 integers you provided:
print(int(num1) * int(num2) * int(num3) * int(num4))
