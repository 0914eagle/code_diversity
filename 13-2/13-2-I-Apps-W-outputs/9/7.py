
def f1(n, x):
    # Initialize variables
    ice_cream = x
    distressed_kids = 0
    
    # Iterate through the queue
    for i in range(n):
        # Read the next operation
        operation = input().split()
        
        # If the operation is "+", a carrier arrives with d ice cream packs
        if operation[0] == "+":
            d = int(operation[1])
            ice_cream += d
        
        # If the operation is "-", a child asks for d ice cream packs
        elif operation[0] == "-":
            d = int(operation[1])
            if ice_cream >= d:
                ice_cream -= d
            else:
                distressed_kids += 1
    
    # Return the number of ice cream packs left and the number of distressed kids
    return ice_cream, distressed_kids

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    n, x = map(int, input().split())
    print(*f1(n, x))

