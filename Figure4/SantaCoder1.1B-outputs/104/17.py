def unique_digits(x):
    
    # Your code here
    return sorted(list(set(x) - set(map(int, str(x)))))

#