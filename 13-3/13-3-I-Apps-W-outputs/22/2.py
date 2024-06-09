
def get_min_number(cnt_1, cnt_2, x, y):
    # Initialize a set to store the numbers that are not liked by either friend
    not_liked = set()
    
    # Iterate through the range of numbers from 1 to x*y
    for i in range(1, x*y+1):
        # If the number is not divisible by x or y, it is liked by both friends
        if i % x != 0 and i % y != 0:
            not_liked.add(i)
    
    # Initialize a set to store the numbers that are liked by the first friend
    liked_1 = set()
    # Iterate through the range of numbers from 1 to x
    for i in range(1, x+1):
        # If the number is not divisible by x, it is liked by the first friend
        if i % x != 0:
            liked_1.add(i)
    
    # Initialize a set to store the numbers that are liked by the second friend
    liked_2 = set()
    # Iterate through the range of numbers from 1 to y
    for i in range(1, y+1):
        # If the number is not divisible by y, it is liked by the second friend
        if i % y != 0:
            liked_2.add(i)
    
    # Initialize a set to store the numbers that are liked by both friends
    liked_both = liked_1 & liked_2
    
    # Initialize a set to store the numbers that are not liked by either friend
    not_liked = not_liked - liked_both
    
    # Find the minimum number of numbers that can be formed using the numbers in the set not_liked
    min_number = min(not_liked)
    
    # Return the minimum number
    return min_number

def main():
    cnt_1, cnt_2, x, y = map(int, input().split())
    print(get_min_number(cnt_1, cnt_2, x, y))

if __name__ == '__main__':
    main()

