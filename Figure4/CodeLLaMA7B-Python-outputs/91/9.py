def is_bored(S):
    
    # your code here
    count = 0
    for i in range(len(S)-2):
        if S[i:i+2] == "I ":
            if S[i+2] == "." or S[i+2] == "?" or S[i+2] == "!":
                count += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
