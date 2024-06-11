def sum_squares(lst):
    
    return sum([x**2 for x in lst if x%3==0 or x%4==0])

print(sum_squares([1,2,3]))
print(sum_squares([]))
print(sum_squares([-1,-5,2,-1,-5]))
