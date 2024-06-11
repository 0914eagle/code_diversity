def sort_even(l: list):
    
    l_even = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_even.append(l[i])
    l_even.sort()
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = l_even[i // 2]
    return l


