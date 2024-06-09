
def get_min_number(cnt_1, cnt_2, x, y):
    # Initialize a set to store the numbers that are not liked by either friend
    not_liked = set()
    
    # Iterate through the numbers from 2 to x and check if they are not divisible by x
    for i in range(2, x):
        if i % x != 0:
            not_liked.add(i)
    
    # Iterate through the numbers from x to y and check if they are not divisible by y
    for i in range(x, y):
        if i % y != 0:
            not_liked.add(i)
    
    # Initialize a set to store the numbers that are liked by both friends
    liked = set()
    
    # Iterate through the numbers from 1 to cnt_1 + cnt_2 and check if they are not liked by either friend
    for i in range(1, cnt_1 + cnt_2 + 1):
        if i not in not_liked:
            liked.add(i)
    
    # Return the minimum number of liked numbers that can be formed using the numbers from 1 to cnt_1 + cnt_2
    return min(liked)

def main():
    cnt_1, cnt_2, x, y = map(int, input().split())
    print(get_min_number(cnt_1, cnt_2, x, y))

if __name__ == '__main__':
    main()

