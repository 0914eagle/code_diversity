
def get_input():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    return n, m, arr

def solve(n, m, arr):
    # Sort the array using a stable sorting algorithm
    arr.sort()
    
    # Initialize a counter to keep track of the number of digits changed
    count = 0
    
    # Iterate through the array and change the digits of the elements as needed
    for i in range(n - 1):
        if arr[i] // 10**(m - 1) == arr[i + 1] // 10**(m - 1):
            count += 1
            arr[i] += 1
    
    # Return the sorted array and the number of digits changed
    return arr, count

def main():
    n, m, arr = get_input()
    sorted_arr, count = solve(n, m, arr)
    print(sorted_arr)
    print(count)

if __name__ == '__main__':
    main()

