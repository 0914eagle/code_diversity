
def get_final_area(n, a, b):
    # Calculate the minimum area needed for the room
    min_area = 6 * n
    
    # Check if the current area is greater than the minimum area
    if a * b >= min_area:
        return a * b
    
    # Check if increasing one side by 1 meter is sufficient
    if a + 1 >= b:
        return (a + 1) * b
    elif b + 1 >= a:
        return a * (b + 1)
    
    # Check if increasing both sides by 1 meter is sufficient
    if a + 1 >= b + 1:
        return (a + 1) * (b + 1)
    else:
        return a * (b + 1)

def get_room_sizes(n, a, b):
    final_area = get_final_area(n, a, b)
    a_1 = final_area // b
    b_1 = final_area // a
    return a_1, b_1

if __name__ == '__main__':
    n, a, b = map(int, input().split())
    a_1, b_1 = get_room_sizes(n, a, b)
    print(a_1, b_1)

