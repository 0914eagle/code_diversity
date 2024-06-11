def solution(lst):
    
    odd_sum = 0
    for i in lst:
        if i % 2 == 0:
            odd_sum += i
    return odd_sum


if