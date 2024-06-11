def unique_digits(x):
    
    # YOUR CODE HERE
    result = []
    for i in x:
        if i % 2 == 0:
            continue
        else:
            result.append(i)
    result.sort()
    return result

# If you'd like to check your implementation, run this cell.
