def unique_digits(x):
    
    # YOUR CODE HERE
    # raise NotImplementedError()
    result = []
    for i in x:
        if not any(int(j) % 2 == 0 for j in str(i)):
            result.append(i)
    return sorted(result)

#