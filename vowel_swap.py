#!/usr/bin/python3

# Vowel Swapper~
# This program takes in a user input from stdin, and swaps all vowel characters found
# Currently only supports 1 word. Use underscores to pass in multiple words

import sys

if len(sys.argv) == 1:
    print("Usage: ./vowel_swap.py WORD")
    exit
else:
    string = sys.argv[1]
    length = len(string)
    new_list = list(string)
    end = length - 1
    begin = 0
    # We assume y is a vowel here, buy y is only a vowel depending on usage
    # For example, Xylophone vs Yosemite
    vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5, 'y': 6}

    print("Input: {}".format(string))
    print("After swapping...")

    # For whatever reason begin is being reset in this loop, so begin was traded out for a dummy variable
    for loop in range (length):
        for end in range (end, begin - 1, -1):
            # Scans dictionary for a match. Much better than 6 if statements in one line
            if new_list[end] in vowels:
                break

        for begin in range (begin + 1, end + 1, 1):
            if new_list[begin] in vowels:
                break
        if begin >= end:
            break

        new_list[end], new_list[begin] = new_list[begin], new_list[end]
        begin = begin + 1
        end = end - 1

    print("Output: {}".format(''.join(new_list)))
