
import math

def number_of_ways(a, c, m):
    mod = 1000000007
    total = a + c + m
    if total == 0:
        return 1
    if a == 0 and c == 0 and m == 0:
        return 0
    if a == 0 and c == 0:
        return m
    if a == 0 and m == 0:
        return c
    if c == 0 and m == 0:
        return a
    if a == 1 and c == 1 and m == 1:
        return 3
    if a == 1 and c == 1:
        return (m * (m - 1)) // 2
    if a == 1 and m == 1:
        return (c * (c - 1)) // 2
    if c == 1 and m == 1:
        return (a * (a - 1)) // 2
    if a == 1:
        return (c * m * (c + m - 1)) // 2
    if c == 1:
        return (a * m * (a + m - 1)) // 2
    if m == 1:
        return (a * c * (a + c - 1)) // 2
    return (a * c * m * (a + b + c - 1)) // 2

