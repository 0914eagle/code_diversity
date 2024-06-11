def by_length(arr):
    
    # Your code here
    # sort the array
    # reverse the array
    # replace each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
    # if the array is empty, return an empty array
    # if the array has any strange number ignore it
    # return the array
    # if the array is empty, return an empty array
    # if the array has any strange number ignore it
    # return the array
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
            else:
                arr.remove(arr[i])
        return arr

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([1, -1 , 55]))
print(by_length([]))
/Python/Python_functions_practice/03_more_fun_with_functions/03_more_fun_with_functions.py
"""
03 - More Fun with Functions!

Now we want to extend our `sum` function by a new parameter, `condition`,
a function that will return the result of our condition
when passed each individual item from the list.

Read more about it here:
https://www.python-course.eu/python3_lambda.php

We will give you several examples that we