

def unique_digits(x):
    
    result = []
    for i in x:
        if not any(j % 2 == 0 for j in str(i)):
            result.append(i)
    return sorted(result)


