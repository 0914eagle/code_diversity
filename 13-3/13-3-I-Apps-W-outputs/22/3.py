
def f1(cnt_1, cnt_2, x, y):
    # Initialize a set to store the numbers that are not liked by either friend
    not_liked = set()

    # Iterate through the range of numbers from 1 to x
    for i in range(1, x):
        # If the number is not divisible by x, add it to the set of not liked numbers
        if i % x != 0:
            not_liked.add(i)

    # Iterate through the range of numbers from x to y
    for i in range(x, y):
        # If the number is not divisible by y, add it to the set of not liked numbers
        if i % y != 0:
            not_liked.add(i)

    # Initialize a set to store the numbers that are liked by both friends
    liked = set()

    # Iterate through the range of numbers from 1 to x
    for i in range(1, x):
        # If the number is divisible by x, add it to the set of liked numbers
        if i % x == 0:
            liked.add(i)

    # Iterate through the range of numbers from x to y
    for i in range(x, y):
        # If the number is divisible by y, add it to the set of liked numbers
        if i % y == 0:
            liked.add(i)

    # Return the minimum number of presents that can be formed using the numbers in the set not_liked and the numbers in the set liked
    return min(len(not_liked) + len(liked), cnt_1 + cnt_2)

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    cnt_1, cnt_2, x, y = map(int, input().split())
    print(f1(cnt_1, cnt_2, x, y))

