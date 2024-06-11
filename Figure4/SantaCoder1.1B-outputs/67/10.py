def fruit_distribution(s,n):
    
    oranges = s.count("oranges")
    apples = s.count("apples")
    mango = s.count("mango")
    return mango - (oranges + apples)

