def sort_even(l: list):
    
    # Your code here
    even_sorted = sorted(l[::2])
    odd_sorted = l[1::2]
    return odd_sorted + even_sorted


