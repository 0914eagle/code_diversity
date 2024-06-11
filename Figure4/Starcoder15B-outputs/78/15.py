def hex_key(num):
    
    hex_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    num = num.upper()
    num_list = list(num)
    num_list = [hex_dict[i] for i in num_list]
    count = 0
    for i in num_list:
        if is_prime(i):
            count += 1
    return count

