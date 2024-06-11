def even_odd_count(num):
    
    # return (len([x for x in str(num) if int(x) % 2 == 0]), len([x for x in str(num) if int(x) % 2 != 0]))
    # return (len([x for x in str(num) if int(x) % 2 == 0]), len([x for x in str(num) if int(x) % 2 != 0]))
    return (sum(int(x) % 2 == 0 for x in str(num)), sum(int(x) % 2 != 0 for x in str(num)))


