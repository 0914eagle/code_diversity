
def f1(N, X, x_list):
    # Sort the list of city coordinates in ascending order
    x_list.sort()
    
    # Initialize the maximum value of D
    D = 0
    
    # Iterate through the list of city coordinates
    for i in range(N):
        # Calculate the distance between the current city and the previous city
        distance = abs(x_list[i] - x_list[i-1])
        
        # Update the maximum value of D if the current distance is greater than the previous value of D
        if distance > D:
            D = distance
    
    return D

def f2(N, X, x_list):
    # Sort the list of city coordinates in ascending order
    x_list.sort()
    
    # Initialize the maximum value of D
    D = 0
    
    # Iterate through the list of city coordinates
    for i in range(N):
        # Calculate the distance between the current city and the previous city
        distance = abs(x_list[i] - x_list[i-1])
        
        # Update the maximum value of D if the current distance is greater than the previous value of D
        if distance > D:
            D = distance
    
    return D

if __name__ == '__main__':
    N, X = map(int, input().split())
    x_list = list(map(int, input().split()))
    print(f1(N, X, x_list))

