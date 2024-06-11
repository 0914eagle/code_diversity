def even_odd_count(num):
    
    # return (len([i for i in str(num) if int(i) % 2 == 0]), len([i for i in str(num) if int(i) % 2 != 0]))
    return (sum(int(i) % 2 == 0 for i in str(num)), sum(int(i) % 2 != 0 for i in str(num)))


