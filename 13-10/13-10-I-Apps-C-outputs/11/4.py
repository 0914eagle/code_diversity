
def get_perfect_squares(arr):
    # create a set to store the perfect squares
    perfect_squares = set()
    for num in arr:
        # check if the number is a perfect square
        root = num ** 0.5
        if root % 1 == 0:
            # if it is a perfect square, add it to the set
            perfect_squares.add(int(root))
    return perfect_squares

def get_largest_not_perfect_square(arr):
    # get the set of perfect squares
    perfect_squares = get_perfect_squares(arr)
    # sort the array in descending order
    arr.sort(reverse=True)
    # find the first number that is not a perfect square
    for num in arr:
        if num not in perfect_squares:
            return num

def main():
    arr = list(map(int, input().split()))
    result = get_largest_not_perfect_square(arr)
    print(result)

if __name__ == '__main__':
    main()

