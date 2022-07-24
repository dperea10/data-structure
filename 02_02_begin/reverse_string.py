"""
Python Data Structures - A Game-Based Approach
Stack challenge
Diego Perea
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.
for char in string:
    s.pop(char)

while not is_empty(reversed_string):
    print(reversed_string)
