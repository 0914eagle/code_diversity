def exchange(lst1, lst2):
    
    # O(n) time, O(1) space
    if len(lst1) != len(lst2):
        return "NO"
    sum1 = sum(lst1)
    sum2 = sum(lst2)
    if sum1 % 2 == 0 and sum2 % 2 == 0:
        return "YES"
    elif sum1 % 2 != 0 and sum2 % 2 != 0:
        return "YES"
    else:
        return "NO"


print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
