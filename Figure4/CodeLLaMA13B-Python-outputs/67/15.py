def fruit_distribution(s,n):
    
    # your code here
    apples = 0
    oranges = 0
    for i in range(len(s)):
        if s[i] == "a":
            apples += 1
        elif s[i] == "o":
            oranges += 1
    return n - apples - oranges


print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))
