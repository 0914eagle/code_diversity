def by_length(arr):
    
    # Your code here
    # 1. sort the array
    # 2. reverse the array
    # 3. replace each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
    # 4. return the array
    # 5. if the array is empty, return an empty array
    # 6. if the array has any strange number ignore it

    # 1. sort the array
    arr.sort()
    # 2. reverse the array
    arr.reverse()
    # 3. replace each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
    # 4. return the array
    return [
        "One" if x == 1 else "Two" if x == 2 else "Three" if x == 3 else "Four" if x == 4 else "Five" if x == 5 else "Six" if x == 6 else "Seven" if x == 7 else "Eight" if x == 8 else "Nine" if x == 9 else "" for x in arr
    ]


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
