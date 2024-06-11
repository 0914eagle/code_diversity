def solution(lst):
    
    # Write your code here
    odd_elements = []
    for i in lst:
        if i % 2 == 1:
            odd_elements.append(i)
    return sum(odd_elements)


if