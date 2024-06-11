def unique_digits(x):
    
    # Your code here
    # 1. Convert all numbers to strings
    # 2. Check if there is any even digit
    # 3. If there is no even digit, add to the result
    # 4. Return the result
    result = []
    for i in x:
        if not any(int(j) % 2 == 0 for j in str(i)):
            result.append(i)
    return sorted(result)


if __name__