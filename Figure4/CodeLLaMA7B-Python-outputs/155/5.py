def even_odd_count(num):
    
    # return (len([d for d in str(num) if int(d) % 2 == 0]), len([d for d in str(num) if int(d) % 2 != 0]))
    even = 0
    odd = 0
    for d in str(num):
        if int(d) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)


