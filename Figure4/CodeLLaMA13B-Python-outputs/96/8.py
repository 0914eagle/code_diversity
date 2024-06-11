def count_up_to(n):
    
    # Your code here
    arr = []
    for i in range(2, n):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                arr.append(i)
    return arr


print(count_up_to(18))
