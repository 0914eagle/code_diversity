
def get_min_number(cnt_1, cnt_2, x, y):
    # Initialize a set to store the numbers that are not liked by either friend
    not_liked = set()
    
    # Iterate through the numbers from 1 to x and find the numbers that are not liked by the first friend
    for i in range(1, x):
        if i % x == 0:
            not_liked.add(i)
    
    # Iterate through the numbers from x to y and find the numbers that are not liked by the second friend
    for i in range(x, y):
        if i % y == 0:
            not_liked.add(i)
    
    # Initialize a set to store the numbers that are liked by both friends
    liked = set()
    
    # Iterate through the numbers from 1 to y and find the numbers that are liked by both friends
    for i in range(1, y):
        if i not in not_liked:
            liked.add(i)
    
    # Return the minimum number of liked numbers that can be formed using the numbers from 1 to v
    return min(liked)

if __name__ == '__main__':
    cnt_1, cnt_2, x, y = map(int, input().split())
    print(get_min_number(cnt_1, cnt_2, x, y))

