
def get_number_of_boxes(n, m, a, X):
    # Calculate the total number of candies in the box
    total_candies = sum(a)
    
    # Initialize a list to store the number of boxes opened for each query
    boxes_opened = []
    
    # Loop through each query
    for x in X:
        # Initialize a variable to store the number of boxes opened for this query
        opened_boxes = 0
        
        # Loop through each level of the box
        for i in range(n):
            # Calculate the number of candies in this level
            candies_in_level = a[i] * (i + 1)
            
            # If the number of candies in this level is greater than or equal to the number of candies needed for this query, break the loop
            if candies_in_level >= x:
                break
            
            # Otherwise, increment the number of boxes opened for this query
            opened_boxes += 1
        
        # Add the number of boxes opened for this query to the list
        boxes_opened.append(opened_boxes)
    
    return boxes_opened

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    X = list(map(int, input().split()))
    boxes_opened = get_number_of_boxes(n, m, a, X)
    for box in boxes_opened:
        print(box)

if __name__ == '__main__':
    main()

