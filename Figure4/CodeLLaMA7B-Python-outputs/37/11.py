def sort_even(l: list):
    
    # Your code here
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    odd_indices = [i for i in range(len(l)) if i % 2 == 1]
    even_values = [l[i] for i in even_indices]
    even_values.sort()
    l_sorted = [even_values[i // 2] if i % 2 == 0 else l[i] for i in range(len(l))]
    return l_sorted


if