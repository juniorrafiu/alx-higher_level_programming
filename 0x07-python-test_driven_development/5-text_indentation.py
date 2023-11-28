#!/usr/bin/python3
""" indent text"""


def text_indentation(text):
    """Prints a text with 2 new lines aftereach of
    these characters: . , ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if (i == '?') or (i == ':') or (i == '.'):
            print({i}.format(i))
            print()
            counter = 1
        else:
            if i == ' ' and counter == 1:
                continue
            else:
                counter = 0
            if i:
                print(i, end="")
