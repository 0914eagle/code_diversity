def solution(lst):
    
    # Write your code here
    odd_elements = []
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            odd_elements.append(lst[i])
    return sum(odd_elements)
