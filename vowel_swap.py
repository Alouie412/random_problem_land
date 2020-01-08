#!/usr/bin/python3

# Vowel Swapper~
# This program takes in a user input from stdin, and swaps all vowel characters found

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

    print("Input: {}".format(string))
    print("After swapping...")

    # For whatever reason begin is being reset in this loop, so begin was traded out for a dummy variable
    for loop in range (length):
        for end in range (end, begin - 1, -1):
            # There is probably a better way to write out this list of conditions
            # We also assume y is a vowel here, but y is only a vowel depending on usage
            # For example, Xylophone vs Yosemite
            if new_list[end] == 'a' or new_list[end] == 'e' or new_list[end] == 'i' or new_list[end] == 'o' or new_list[end] == 'u' or new_list[end] == 'y':
                break

        for begin in range (begin + 1, end + 1, 1):
            if new_list[begin] == 'a' or new_list[begin] == 'e' or new_list[begin] == 'i' or new_list[begin] == 'o' or new_list[begin] == 'u' or new_list[begin] == 'y':
                break
        if begin >= end:
            break

        new_list[end], new_list[begin] = new_list[begin], new_list[end]
        begin = begin + 1
        end = end - 1

    print("Output: {}".format(''.join(new_list)))
