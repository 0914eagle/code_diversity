def unique_digits(x):
    
    # Your code here
    # unique_digits = []
    # for i in x:
    #     if not any(int(j) % 2 == 0 for j in str(i)):
    #         unique_digits.append(i)
    # return sorted(unique_digits)
    return sorted(i for i in x if not any(int(j) % 2 == 0 for j in str(i)))


if __name__ == "__main