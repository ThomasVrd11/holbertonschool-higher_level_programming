#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        char1 = None
    else:
        char1 = sentence[0]
    return (len(sentence), char1)
