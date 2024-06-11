def eat(number, need, remaining):
    
    return [number + need, remaining - need] if remaining >= need else [number + remaining, 0]
/7kyu/find-the-capitals.py
# https://www.