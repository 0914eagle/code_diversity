def by_length(arr):
    
    # TODO: Write your solution here
    # 1. Sort the array
    arr.sort()
    # 2. Reverse the array
    arr.reverse()
    # 3. Replace each digit by its corresponding name
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


# print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
# print(by_length([]))
# print(by_length([1, -1 , 55]))


