#!/usr/bin/python3
"""
Print text with two new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':'.

    Args:
        text: string to process

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    seps = {'.', '?', ':'}
    segment = ""
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]
        if ch in seps:
            line = segment.strip() + ch
            print(line)
            print()
            segment = ""
            i += 1
            while i < n and text[i] == ' ':
                i += 1
            continue
        else:
            segment += ch
            i += 1

    tail = segment.strip()
    if tail != "":
        print(tail, end="")
