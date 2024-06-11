def sort_third(l: list):
    
    l_prime = l[:]
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime[i] = sorted(l[i:i+3])
    return l_prime

