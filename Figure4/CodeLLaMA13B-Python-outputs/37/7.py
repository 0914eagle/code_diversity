def sort_even(l: list):
    
    # Your code here
    if len(l) == 0:
        return l
    else:
        even_sorted = sort_even(l[2:])
        if l[1] < l[0]:
            return [l[1], l[0]] + even_sorted
        else:
            return [l[0], l[1]] + even_sorted


if