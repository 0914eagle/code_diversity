
def f1(n, x):
    # Initialize variables
    ice_cream = x
    distressed_kids = 0
    
    # Iterate through the queue
    for i in range(n):
        # If the current person is a carrier, add their ice cream to the total
        if i % 2 == 0:
            ice_cream += int(input())
        # If the current person is a child, try to give them ice cream
        else:
            d = int(input())
            if ice_cream >= d:
                ice_cream -= d
            else:
                distressed_kids += 1
    
    # Return the number of ice cream packs left and the number of distressed kids
    return ice_cream, distressed_kids

def f2(...):
    # Implement function 2 here
    pass

if __name__ == '__main__':
    n, x = map(int, input().split())
    print(*f1(n, x))

