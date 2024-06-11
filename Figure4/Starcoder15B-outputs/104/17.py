def unique_digits(x):
    
    # Your code here
    return [i for i in x if not any(int(j) % 2 == 0 for j in str(i))]

# Problem 10
