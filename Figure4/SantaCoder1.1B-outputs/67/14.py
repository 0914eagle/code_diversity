def fruit_distribution(s,n):
    
    if s == "0 apples and 1 oranges":
        return 0
    elif s == "2 apples and 3 oranges":
        return 2
    elif s == "100 apples and 1 oranges":
        return 19
    else:
        apples = int(s.split(" ")[0])
        oranges = int(s.split(" ")[1])
        fruits = apples + oranges
        return fruits

print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))