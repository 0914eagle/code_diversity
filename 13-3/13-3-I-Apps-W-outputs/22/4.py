
def get_min_number(cnt_1, cnt_2, x, y):
    # Initialize a set to store the numbers that are not liked by both friends
    liked_numbers = set(range(1, 10**9 + 1))

    # Remove the numbers that are not liked by the first friend
    for i in range(2, x):
        if x % i == 0:
            liked_numbers.remove(i)

    # Remove the numbers that are not liked by the second friend
    for i in range(x, y):
        if i % x == 0:
            liked_numbers.remove(i)

    # Return the minimum number of liked numbers that can be given to both friends
    return min(len(liked_numbers), cnt_1 + cnt_2)

if __name__ == '__main__':
    cnt_1, cnt_2, x, y = map(int, input().split())
    print(get_min_number(cnt_1, cnt_2, x, y))

