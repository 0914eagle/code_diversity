
def get_non_perfect_square(arr):
    # iterate through the array and check if each element is a perfect square
    for i in range(len(arr)):
        # check if the element is a perfect square
        is_perfect_square = True
        for j in range(1, int(arr[i]**0.5) + 1):
            if arr[i] == j**2:
                is_perfect_square = False
                break
        # if the element is not a perfect square, return it
        if not is_perfect_square:
            return arr[i]
    # if all elements are perfect squares, return None
    return None

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    result = get_non_perfect_square(arr)
    print(result)

if __name__ == '__main__':
    main()

