
def get_min_moves(arr, m):
    # Calculate the current count of elements with each remainder
    count = [0] * m
    for i in range(len(arr)):
        count[(arr[i] % m)] += 1
    
    # Calculate the minimum number of moves required to make the count equal for each remainder
    min_moves = [0] * m
    for i in range(m):
        min_moves[i] = abs(count[i] - len(arr) // m)
    
    # Return the minimum number of moves required to make the count equal for each remainder
    return sum(min_moves)

def get_new_array(arr, m):
    # Calculate the current count of elements with each remainder
    count = [0] * m
    for i in range(len(arr)):
        count[(arr[i] % m)] += 1
    
    # Calculate the minimum number of moves required to make the count equal for each remainder
    min_moves = [0] * m
    for i in range(m):
        min_moves[i] = abs(count[i] - len(arr) // m)
    
    # Create a new array with the minimum number of moves required to make the count equal for each remainder
    new_arr = []
    for i in range(m):
        for j in range(min_moves[i]):
            new_arr.append(arr[i] + (j + 1))
    
    # Return the new array
    return new_arr

if __name__ == '__main__':
    arr = [3, 2, 0, 6, 10, 12]
    m = 3
    print(get_min_moves(arr, m))
    print(get_new_array(arr, m))

