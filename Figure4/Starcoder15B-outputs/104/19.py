def unique_digits(x):
    
    # Your code here
    result = []
    for i in x:
        if i % 2 == 0:
            continue
        else:
            result.append(i)
    return sorted(result)

if __name__ == '__main__':