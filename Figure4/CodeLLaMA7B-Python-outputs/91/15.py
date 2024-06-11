def is_bored(S):
    
    # your code here
    count = 0
    for i in range(len(S)):
        if S[i] == "I":
            count += 1
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
