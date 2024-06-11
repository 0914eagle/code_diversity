def even_odd_count(num):
    
    return (sum(int(i) for i in str(num)), sum(int(i) for i in str(num) if i % 2 == 0))


