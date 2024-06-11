def solution(lst):
    
    odd_elements = []
    for i in lst:
        if i % 2 == 0:
            odd_elements.append(i)
    return sum(odd_elements)


if