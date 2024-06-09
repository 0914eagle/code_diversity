
def get_min_number(cnt_1, cnt_2, x, y):
    # Initialize a set to store the numbers that are not liked by both friends
    liked_numbers = set(range(1, x * y + 1))

    # Remove the numbers that are not liked by the first friend
    for i in range(x, x * y + 1, x):
        liked_numbers.remove(i)

    # Remove the numbers that are not liked by the second friend
    for i in range(y, x * y + 1, y):
        liked_numbers.remove(i)

    # Return the minimum number of liked numbers that can be formed
    return min(liked_numbers)

if __name__ == '__main__':
    cnt_1, cnt_2, x, y = map(int, input().split())
    print(get_min_number(cnt_1, cnt_2, x, y))

