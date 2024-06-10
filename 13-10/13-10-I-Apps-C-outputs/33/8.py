
def count_sets(points, l, r, a):
    # Initialize a set to store the points inside the area
    inside_area = set()
    
    # Iterate through the points and check if they are inside the area
    for point in points:
        if l < point[0] < r and point[1] > a:
            inside_area.add(point)
    
    # Initialize a set to store the points outside the area
    outside_area = set(points) - inside_area
    
    # Initialize a counter to store the number of different non-empty sets
    num_sets = 0
    
    # Iterate through the points inside the area and check if they are part of a different set
    for point in inside_area:
        # Create a copy of the current set and remove the current point
        current_set = inside_area.copy()
        current_set.remove(point)
        
        # Check if the current set is disjoint from any of the outside sets
        is_disjoint = True
        for outside_set in outside_area:
            if outside_set & current_set:
                is_disjoint = False
                break
        
        # If the current set is disjoint from all outside sets, increment the counter
        if is_disjoint:
            num_sets += 1
    
    return num_sets

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    l, r, a = map(int, input().split())
    print(count_sets(points, l, r, a))

if __name__ == '__main__':
    main()

