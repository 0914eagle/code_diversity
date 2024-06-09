
def get_candies(boxes, X):
    # Initialize a list to store the number of candies in each box
    candies = [0] * len(boxes)
    # Initialize a list to store the number of boxes in each level
    levels = [0] * len(boxes)
    
    # Fill in the candies and levels lists
    for i in range(len(boxes)):
        candies[i] = boxes[i]
        levels[i] = 1
    
    # Loop through the boxes and update the candies and levels lists
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            if boxes[j] % boxes[i] == 0:
                candies[j] += candies[i]
                levels[j] += levels[i]
    
    # Find the minimum number of boxes needed to retrieve at least X candies
    min_boxes = float('inf')
    for i in range(len(boxes)):
        if candies[i] >= X:
            min_boxes = min(min_boxes, levels[i])
    
    return min_boxes

def main():
    n, m = map(int, input().split())
    boxes = list(map(int, input().split()))
    X = list(map(int, input().split()))
    
    for x in X:
        print(get_candies(boxes, x))

if __name__ == '__main__':
    main()

