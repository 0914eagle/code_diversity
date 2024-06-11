def sum_squares(lst):
    
    sum = 0
    for i in lst:
        if i % 3 == 0:
            sum += i ** 2
        elif i % 4 == 0:
            sum += i ** 3
    return sum

print(sum_squares([1,2,3]))
print(sum_squares([]))
print(sum_squares([-1,-5,2,-1,-5]))