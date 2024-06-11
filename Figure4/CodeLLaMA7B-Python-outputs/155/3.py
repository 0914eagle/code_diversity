def even_odd_count(num):
    
    # return (len([i for i in str(num) if int(i) % 2 == 0]), len([i for i in str(num) if int(i) % 2 != 0]))
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)


