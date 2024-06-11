def exchange(lst1, lst2):
    
    # Your code here
    lst1_even = []
    lst2_even = []
    for i in lst1:
        if i % 2 == 0:
            lst1_even.append(i)
    for i in lst2:
        if i % 2 == 0:
            lst2_even.append(i)
    if len(lst1_even) == len(lst2_even):
        return "YES"
    else:
        return "NO"


# Tests
assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 3, 4, 5]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 3, 4, 5, 6]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8,