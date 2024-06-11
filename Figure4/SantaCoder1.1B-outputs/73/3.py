def smallest_change(arr):
    
    # Write your code here.
    if len(arr) == 1:
        return 0
    else:
        return min(smallest_change(arr[1:]), smallest_change(arr[:-1])) + 1


if __name__ == "__main__":
    print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
    print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
    print(smallest_change([1, 2, 3, 2, 1]))
    print(smallest_change([1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
