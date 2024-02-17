#!/usr/bin/env python3
from os import close


words = set()


def check(word):
    if word.lower() in words:
        return True
    else:
        return False


def load(dictonary):
    file = open(dictonary, "r")
    for line in file:
        word = line.rstrip()
        words.add(line)
    close(file)
    return True


def size():
    return len(words)


def unload():
    return True
