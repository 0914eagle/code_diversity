
def get_min_boxes(n, m, a, X):
    # Initialize a list to store the number of boxes at each level
    boxes = [0] * (n + 1)
    boxes[0] = 1
    
    # Calculate the total number of boxes at each level
    for i in range(1, n + 1):
        boxes[i] = boxes[i - 1] * a[i - 1]
    
    # Initialize a list to store the minimum number of boxes needed to retrieve X candies
    min_boxes = [0] * m
    
    # Loop through each query and calculate the minimum number of boxes needed
    for i in range(m):
        # Initialize a variable to store the total number of candies
        total_candies = 0
        
        # Loop through each level and calculate the number of candies at that level
        for j in range(n, -1, -1):
            total_candies += boxes[j] * X[i] // boxes[0]
            if total_candies >= X[i]:
                break
        
        # Calculate the minimum number of boxes needed to retrieve X[i] candies
        min_boxes[i] = boxes[j] - (total_candies - X[i]) // boxes[j - 1]
    
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

