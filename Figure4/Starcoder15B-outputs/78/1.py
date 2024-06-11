def hex_key(num):
    
    primes = [2, 3, 5, 7, 11, 13, 17]
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hex_list = list(num)
    hex_list = [hex_dict[i] for i in hex_list]
    count = 0
    for i in hex_list:
        if i in primes:
            count += 1
    return count

