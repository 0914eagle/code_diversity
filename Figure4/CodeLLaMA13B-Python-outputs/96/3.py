def count_up_to(n):
    
    # Your code here
    if n <= 1:
        return []
    prime_list = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list


print(count_up_to(18))
