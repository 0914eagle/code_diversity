def even_odd_count(num):
    
    # return (sum(int(i) % 2 == 0 for i in str(num)), sum(int(i) % 2 != 0 for i in str(num)))
    # return (sum(int(i) % 2 == 0 for i in str(num)), len(str(num)) - sum(int(i) % 2 == 0 for i in str(num)))
    # return (sum(int(i) % 2 == 0 for i in str(num)), len(str(num)) - sum(int(i) % 2 != 0 for i in str(num)))
    return (sum(int(i) % 2 == 0 for i in str(num)), len(str(num)) - sum(int(i) % 2 == 0 for i in str(num)))


