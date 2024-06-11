def sort_third(l: list):
    
    # Your code here
    l_prime = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime.append(sorted(l[i::3]))
        else:
            l_prime.append(l[i])
    return l_prime


