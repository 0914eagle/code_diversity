
import math

def solve(n, boxes):
    # Initialize the answer and the maximum number of boxes in a pile
    answer = 0
    max_boxes = 0
    
    # Iterate over all possible piles
    for i in range(1 << n):
        # Initialize the current pile and the number of boxes in it
        pile = []
        num_boxes = 0
        
        # Iterate over all boxes
        for j in range(n):
            # If the j-th bit of the current pile is set, add the j-th box to the pile
            if i & (1 << j):
                pile.append(boxes[j])
                num_boxes += 1
        
        # If the current pile has the maximum number of boxes, update the answer
        if num_boxes > max_boxes:
            max_boxes = num_boxes
            answer = 1
        # If the current pile has the same number of boxes as the maximum pile, update the answer
        elif num_boxes == max_boxes:
            answer += 1
    
    # Return the answer modulo 10^9 + 7
    return answer % (10**9 + 7)

