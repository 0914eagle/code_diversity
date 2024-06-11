def sum_squares(lst):
    
    # Solution
    lst_squares = [i**2 for i in lst if i%3 == 0]
    lst_cubes = [i**3 for i in lst if i%4 == 0 and i%3 != 0]
    return sum(lst_squares + lst_cubes)
    
    
    
# Test Cases

print(sum_squares([1, 2, 3]))
print(sum_squares([]))
print(sum_squares([-1, -5, 2, -1, -5]))
