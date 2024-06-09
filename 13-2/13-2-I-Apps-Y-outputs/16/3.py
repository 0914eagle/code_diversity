
def f1(n, V):
    # Initialize an empty list to store the volumes of the boxes
    volumes = []
    
    # Iterate through the input and append the volumes of each box to the list
    for i in range(n):
        l, w, h = map(int, input().split())
        volumes.append(l * w * h)
    
    # Find the largest volume and calculate the difference between it and V
    largest_volume = max(volumes)
    difference = largest_volume - V
    
    # Return the difference
    return difference

def f2(...):
    # Implement function 2 here
    pass

if __name__ == '__main__':
    n = int(input())
    V = int(input())
    
    # Call function 1 and print the result
    result = f1(n, V)
    print(result)

