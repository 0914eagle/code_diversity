def unique_digits(x):
    
    # TODO: Write your code here.
    return sorted(x, key=lambda x: int(str(x)[-1]))


