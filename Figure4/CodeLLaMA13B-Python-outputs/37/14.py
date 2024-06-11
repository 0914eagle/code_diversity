def sort_even(l: list):
    
    # Your code here
    even_sorted = []
    for i in range(0, len(l), 2):
        even_sorted.append(l[i])
    even_sorted.sort()
    for i in range(0, len(l), 2):
        l[i] = even_sorted[i // 2]
    return l


if __name__