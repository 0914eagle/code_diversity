def eat(number, need, remaining):
    
    return [number + need, remaining - need] if remaining >= need else [number + remaining, 0]

# Test
print(eat(5, 6,