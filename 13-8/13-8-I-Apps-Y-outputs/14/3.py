
import re

def solve(L):
    L = L.strip()
    opening_delimiters = ["(", "[", "{"]
    closing_delimiters = [")", "]", "}"]
    stack = []
    for i, char in enumerate(L):
        if char in opening_delimiters:
            stack.append(char)
        elif char in closing_delimiters:
            if not stack or opening_delimiters.index(stack.pop()) != closing_delimiters.index(char):
                return f"{char} {i}"
    if stack:
        return "ok so far"
    else:
        return "ok so far"

