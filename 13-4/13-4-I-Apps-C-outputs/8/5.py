
def f1(n, A, B, intersections):
    # Initialize a dictionary to store the distances from each intersection to the leaning tower
    distances = {}
    for i in range(n):
        distances[i] = 0
    
    # Initialize a queue to store the intersections to be processed
    queue = []
    
    # Enqueue the starting points
    queue.append(A)
    queue.append(B)
    
    # Loop until the queue is empty
    while queue:
        # Dequeue an intersection
        intersection = queue.pop(0)
        
        # If the intersection is the leaning tower, return the distance
        if intersections[intersection][2] == 1:
            return distances[intersection]
        
        # If the intersection has not been processed before, process it
        if distances[intersection] == 0:
            # Get the left and right neighbors
            left = intersections[intersection][0]
            right = intersections[intersection][1]
            
            # Enqueue the left and right neighbors
            queue.append(left)
            queue.append(right)
            
            # Update the distance for the left and right neighbors
            distances[left] = distances[intersection] + 1
            distances[right] = distances[intersection] + 1
    
    # If the queue is empty and the leaning tower has not been found, return indistinguishable
    return "indistinguishable"

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    A = int(input())
    B = int(input())
    intersections = []
    for i in range(n):
        intersections.append(list(map(int, input().split())))
    print(f1(n, A, B, intersections))

