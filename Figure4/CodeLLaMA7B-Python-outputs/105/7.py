def by_length(arr):
    
    # 1. sort the integers that are between 1 and 9 inclusive
    arr.sort()
    # 2. reverse the resulting array
    arr.reverse()
    # 3. replace each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".
    # 3.1 create a dictionary to map the number to its name
    num_to_name = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    # 3.2 replace each digit by its corresponding name
    for i in range(len(arr)):
        if arr[i] in num_to_name:
            arr[i] = num_to_name[arr[i]]
    return arr


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
