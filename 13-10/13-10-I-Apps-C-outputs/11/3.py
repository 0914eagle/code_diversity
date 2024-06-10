
def get_non_perfect_square(arr):
    # find all perfect squares in the array
    perfect_squares = []
    for i in range(len(arr)):
        if is_perfect_square(arr[i]):
            perfect_squares.append(arr[i])
    
    # find the largest number in the array that is not a perfect square
    max_value = -1
    for i in range(len(arr)):
        if arr[i] not in perfect_squares and arr[i] > max_value:
            max_value = arr[i]
    
    return max_value

def is_perfect_square(n):
    # check if n is a perfect square
    x = int(n**0.5)
    return x**2 == n

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_non_perfect_square(arr))

