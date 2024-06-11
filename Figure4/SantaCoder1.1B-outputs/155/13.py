def even_odd_count(num):
    
    return (sum(1 for i in range(1, len(str(num))) if num % 10 == int(str(num)[i])))


