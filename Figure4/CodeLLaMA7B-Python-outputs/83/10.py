def starts_one_ends(n):
    
    # 10**(n-1) is the largest n-digit number
    return sum(int(str(i).startswith('1')) + int(str(i).endswith('1'))
               for i in range(1, 10**(n-1)+1))


