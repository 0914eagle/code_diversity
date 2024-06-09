
def get_minimum_moves(n, m, arr):
    # Calculate the current count of elements with each remainder
    count = [0] * m
    for i in range(n):
        count[(arr[i] % m)] += 1
    
    # Calculate the minimum number of moves required to make the count equal for each remainder
    min_moves = [0] * m
    for i in range(m):
        min_moves[i] = abs(count[i] - n//m)
    
    # Return the minimum number of moves required to make the count equal for each remainder
    return sum(min_moves)

def get_new_array(n, m, arr):
    # Calculate the current count of elements with each remainder
    count = [0] * m
    for i in range(n):
        count[(arr[i] % m)] += 1
    
    # Calculate the minimum number of moves required to make the count equal for each remainder
    min_moves = [0] * m
    for i in range(m):
        min_moves[i] = abs(count[i] - n//m)
    
    # Create a new array with the minimum number of moves required to make the count equal for each remainder
    new_arr = [0] * n
    for i in range(n):
        new_arr[i] = arr[i] + min_moves[(arr[i] % m)]
    
    # Return the new array
    return new_arr

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_minimum_moves(n, m, arr))
    print(*get_new_array(n, m, arr))

