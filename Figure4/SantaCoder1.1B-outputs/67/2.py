def fruit_distribution(s,n):
    
    apples = s.count("apples")
    oranges = s.count("oranges")
    mango = s.count("mango")
    return mango - (apples + oranges)

