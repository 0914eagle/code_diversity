def hex_key(num):
    
    # Your code here
    num = num.upper()
    num_list = list(num)
    prime_list = []
    for i in range(len(num_list)):
        if num_list[i] == 'A' or num_list[i] == 'B' or num_list[i] == 'C' or num_list[i] == 'D' or num_list[i] == 'E' or num_list[i] == 'F':
            prime_list.append(num_list[i])
    prime_list.sort()
    prime_list.reverse()
    count = 0
    for i in range(len(prime_list)):
        if prime_list[i] == 'A' or prime_list[i] == 'B' or prime_list[i] == 'C' or prime_list[i] == 'D' or prime_list[i] == 'E' or prime_list[i] == 'F':
            count += 1
    return count

