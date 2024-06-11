def unique_digits(x):
    
    # Your code here
    return sorted(list(set(x) - set(map(lambda x: int(str(x)[0]), x))))

#