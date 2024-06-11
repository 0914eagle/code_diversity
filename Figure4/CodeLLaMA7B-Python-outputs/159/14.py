def eat(number, need, remaining):
    
    return [number + remaining, max(0, remaining - need)]


# TESTS
assert eat(5, 6, 10) == [11, 4]
assert eat(4, 8, 9) == [12, 1]
assert eat(1, 10, 10) == [11, 0]
assert eat(2, 11, 5) == [7, 0]