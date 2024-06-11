def fruit_distribution(s,n):
    
    # Your code here
    if s.count("apples") > s.count("oranges"):
        return s.count("apples") - s.count("oranges")
    else:
        return s.count("oranges") - s.count("apples")

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))
