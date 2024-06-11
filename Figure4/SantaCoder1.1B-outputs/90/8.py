def next_smallest(lst):
    
    # Your code here
    lst.sort()
    if len(lst) == 0:
        return None
    else:
        return lst[1]

print(next_smallest([1, 2, 3, 4, 5]))
print(next_smallest([5, 1, 4, 3, 2]))
print(next_smallest([]))
print(next_smallest([1, 1]))