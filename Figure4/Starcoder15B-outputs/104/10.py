def unique_digits(x):
    
    # Your code here
    return [i for i in x if all(int(j)%2!=0 for j in str(i))]

if __name__ == '__main__':
    import doctest
    do