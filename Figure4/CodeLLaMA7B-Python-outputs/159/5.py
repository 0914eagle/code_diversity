def eat(number, need, remaining):
    
    if need > remaining:
        return [number + remaining, 0]
    else:
        return [number + need, remaining - need]


print(eat(5, 6, 10))
print(eat(4, 8, 9))
print(eat(1, 10, 10))
print(eat(2, 11, 5))
