
def f1(n, q, x_coords, y_coords, a, b):
    # Find the minimum side length of the square
    side_length = min(max(x_coords), max(y_coords)) + 1
    
    # Initialize a set to store the addresses of the houses in the range [a, b]
    house_set = set(range(a, b + 1))
    
    # Iterate through the houses and check if they are in the range [a, b]
    for i in range(n):
        if i in house_set:
            # If the house is in the range, remove it from the set
            house_set.remove(i)
            # If the set is empty, break the loop
            if not house_set:
                break
    
    # If the set is not empty, return 0 as the answer
    if house_set:
        return 0
    else:
        # Return the side length of the square
        return side_length

def f2(...):
    # Implement function 2 here
    pass

if __name__ == '__main__':
    n, q = map(int, input().split())
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    for i in range(q):
        a, b = map(int, input().split())
        print(f1(n, q, x_coords, y_coords, a, b))

