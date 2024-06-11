def pluck(arr):
    
    if not arr:
        return []

    smallest_even_value = min([x for x in arr if x % 2 == 0])
    smallest_even_index = arr.index(smallest_even_value)

    return [smallest_even_value, smallest_even_index]


print(pluck([4,2,3]))
print(pluck([1,2,3]))
print(pluck([]))
print(pluck([5, 0, 3, 0, 4, 2]))
