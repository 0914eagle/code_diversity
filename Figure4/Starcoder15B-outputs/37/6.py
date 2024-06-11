def sort_even(l: list):
    
    l_even = [l[i] for i in range(len(l)) if i % 2 == 0]
    l_even.sort()
    l_odd = [l[i] for i in range(len(l)) if i % 2 == 1]
    return [l_even[i//2] if i % 2 == 0 else l_odd[i//2] for i in range(len(l))]

