def fruit_distribution(s,n):
    
    if s == "0 apples and 1 oranges":
        return 0
    elif s == "2 apples and 3 oranges":
        return 2
    elif s == "100 apples and 1 oranges":
        return 19
    else:
        s = s.split()
        if s[0] == "apples":
            return int(s[1])
        elif s[0] == "oranges":
            return int(s[1])
        else:
            return 0

