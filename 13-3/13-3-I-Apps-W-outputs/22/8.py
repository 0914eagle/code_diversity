
def get_min_number(cnt_1, cnt_2, x, y):
    # Initialize a set to store the numbers that are not liked by either friend
    not_liked = set()
    
    # Iterate through the range of numbers from 1 to the maximum number that can be presented
    for i in range(1, cnt_1 + cnt_2 + 1):
        # If the number is not divisible by x or y, it is a valid number
        if i % x != 0 and i % y != 0:
            not_liked.add(i)
    
    # Initialize a set to store the numbers that are presented to the first friend
    first_friend = set()
    # Iterate through the range of numbers from 1 to the number of numbers presented to the first friend
    for i in range(1, cnt_1 + 1):
        # If the number is in the set of not liked numbers, add it to the set of numbers presented to the first friend
        if i in not_liked:
            first_friend.add(i)
    
    # Initialize a set to store the numbers that are presented to the second friend
    second_friend = set()
    # Iterate through the range of numbers from 1 to the number of numbers presented to the second friend
    for i in range(1, cnt_2 + 1):
        # If the number is in the set of not liked numbers, add it to the set of numbers presented to the second friend
        if i in not_liked:
            second_friend.add(i)
    
    # Return the minimum number that can be formed using the numbers presented to the two friends
    return min(first_friend | second_friend)

if __name__ == '__main__':
    cnt_1, cnt_2, x, y = map(int, input().split())
    print(get_min_number(cnt_1, cnt_2, x, y))

