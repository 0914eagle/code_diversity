def fruit_distribution(s,n):
    
    # your code goes here
    s = s.split()
    apples = int(s[0])
    oranges = int(s[4])
    mangoes = n - apples - oranges
    return mangoes

# test cases
print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples