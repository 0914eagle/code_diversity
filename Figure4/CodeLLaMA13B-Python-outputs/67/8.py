def fruit_distribution(s,n):
    
    # your code here
    return n - int(s.split()[0]) - int(s.split()[2])



print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))
