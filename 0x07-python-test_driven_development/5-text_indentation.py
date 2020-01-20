#!/usr/bin/python3
def text_indentation(text):

    if type(text) is not str:
        raise TypeError('text must be a string')
    i = 0
    while i < (len(text)):
        if text[i] != '\n':
            print (text[i], end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('\n' * 2, end="")
            if text[i+1] == " ":
                i = i+1
        i = i+1
