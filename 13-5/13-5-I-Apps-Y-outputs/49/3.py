
def get_adjacent_replacements(arr):
    # Create a copy of the array
    arr_copy = arr[:]
    
    # Iterate through the array and replace each occurrence of 1 with 2
    for i in range(len(arr_copy)):
        if arr_copy[i] == 1:
            arr_copy[i] = 2
    
    # Iterate through the array and replace each occurrence of 2 with 1
    for i in range(len(arr_copy)):
        if arr_copy[i] == 2:
            arr_copy[i] = 1
    
    # Iterate through the array and replace each occurrence of 3 with 4
    for i in range(len(arr_copy)):
        if arr_copy[i] == 3:
            arr_copy[i] = 4
    
    # Iterate through the array and replace each occurrence of 4 with 3
    for i in range(len(arr_copy)):
        if arr_copy[i] == 4:
            arr_copy[i] = 3
    
    # Iterate through the array and replace each occurrence of 5 with 6
    for i in range(len(arr_copy)):
        if arr_copy[i] == 5:
            arr_copy[i] = 6
    
    # Iterate through the array and replace each occurrence of 6 with 5
    for i in range(len(arr_copy)):
        if arr_copy[i] == 6:
            arr_copy[i] = 5
    
    # Iterate through the array and replace each occurrence of 7 with 8
    for i in range(len(arr_copy)):
        if arr_copy[i] == 7:
            arr_copy[i] = 8
    
    # Iterate through the array and replace each occurrence of 8 with 7
    for i in range(len(arr_copy)):
        if arr_copy[i] == 8:
            arr_copy[i] = 7
    
    # Iterate through the array and replace each occurrence of 9 with 10
    for i in range(len(arr_copy)):
        if arr_copy[i] == 9:
            arr_copy[i] = 10
    
    # Iterate through the array and replace each occurrence of 10 with 9
    for i in range(len(arr_copy)):
        if arr_copy[i] == 10:
            arr_copy[i] = 9
    
    return arr_copy

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = get_adjacent_replacements(arr)
    print(*result)

if __name__ == '__main__':
    main()

