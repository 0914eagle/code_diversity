
def find_common_element(list1, list2):
    return list(set(list1).intersection(list2))

def find_agreement(x_coords, y_coords, x, y):
    # Find the median of the x-coordinates
    x_median = sum(x_coords) // len(x_coords)
    
    # Find the median of the y-coordinates
    y_median = sum(y_coords) // len(y_coords)
    
    # Find the difference between the x-median and the y-median
    diff = abs(x_median - y_median)
    
    # If the difference is less than or equal to the distance between x and y, they will come to an agreement
    if diff <= abs(x - y):
        return True
    else:
        return False

def main():
    n, m, x, y = map(int, input().split())
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    
    if find_common_element(x_coords, y_coords):
        print("No War")
    else:
        if find_agreement(x_coords, y_coords, x, y):
            print("No War")
        else:
            print("War")

if __name__ == '__main__':
    main()

