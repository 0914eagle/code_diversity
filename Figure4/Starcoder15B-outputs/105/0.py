def by_length(arr):
    
    # Your code here
    if len(arr) == 0:
        return []
    else:
        arr.sort()
        arr.reverse()
        for i in range(len(arr)):
            if arr[i] == 1:
                arr[i] = "One"
            elif arr[i] == 2:
                arr[i] = "Two"
            elif arr[i] == 3:
                arr[i] = "Three"
            elif arr[i] == 4:
                arr[i] = "Four"
            elif arr[i] == 5:
                arr[i] = "Five"
            elif arr[i] == 6:
                arr[i] = "Six"
            elif arr[i] == 7:
                arr[i] = "Seven"
            elif arr[i] == 8:
                arr[i] = "Eight"
            elif arr[i] == 9:
                arr[i] = "Nine"
        return arr

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1 , 55]))
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(by_length([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(by_length([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(by_length([1, 2, 3, 4