
def get_min_boxes(n, m, a, X):
    # Initialize a list to store the number of boxes at each level
    num_boxes = [0] * (n + 1)
    num_boxes[0] = 1
    
    # Calculate the number of boxes at each level using the recurrence relation
    for i in range(1, n + 1):
        num_boxes[i] = num_boxes[i - 1] * a[i - 1]
    
    # Initialize a list to store the minimum number of boxes needed to retrieve X candies
    min_boxes = [0] * m
    
    # Loop through each query and calculate the minimum number of boxes needed to retrieve X candies
    for i in range(m):
        # Initialize a variable to store the total number of candies
        total_candies = 0
        
        # Loop through each level and calculate the number of candies at each level
        for j in range(n, -1, -1):
            total_candies += num_boxes[j] * X[i] // num_boxes[j - 1]
        
        # Calculate the minimum number of boxes needed to retrieve X candies
        min_boxes[i] = total_candies // X[i]
    
    return min_boxes

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    X = list(map(int, input().split()))
    min_boxes = get_min_boxes(n, m, a, X)
    for i in range(m):
        print(min_boxes[i])

if __name__ == '__main__':
    main()

