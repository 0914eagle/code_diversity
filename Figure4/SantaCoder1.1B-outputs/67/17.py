def fruit_distribution(s,n):
    
    apples = 0
    oranges = 0
    mango = 0
    for i in s:
        if i == "a":
            apples += 1
        elif i == "o":
            oranges += 1
        elif i == "m":
            mango += 1
    return apples + oranges - mango

print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))
