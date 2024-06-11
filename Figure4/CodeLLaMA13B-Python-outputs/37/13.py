def sort_even(l: list):
    
    # Your code here
    even = []
    odd = []
    for i in range(len(l)):
        if i % 2 == 0:
            even.append(l[i])
        else:
            odd.append(l[i])
    even.sort()
    l = []
    for i in range(len(even)):
        l.append(even[i])
        l.append(odd[i])
    return l


if