def unique_digits(x):
    
    # Your code here
    result = []
    for i in x:
        if i % 2 != 0:
            result.append(i)
    return result

if __name__ == '__main__':
   