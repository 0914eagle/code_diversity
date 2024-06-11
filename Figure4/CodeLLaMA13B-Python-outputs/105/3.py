def by_length(arr):
    
    # Your code here
    # 1. sort the array
    # 2. reverse the array
    # 3. replace each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    # 4. return the array
    # 5. if the array is empty, return an empty array
    # 6. if the array has any strange number ignore it

    # 1. sort the array
    arr.sort()
    # 2. reverse the array
    arr.reverse()
    # 3. replace each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
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
        else:
            arr.pop(i)
    # 4. return the array
    return arr


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
