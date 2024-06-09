
def get_fibonacci_tour(n, m, heights, roads):
    # Initialize a dictionary to store the mansion heights and the mansion indices
    mansion_heights = {i: heights[i-1] for i in range(1, n+1)}
    mansion_indices = {heights[i-1]: i for i in range(1, n+1)}
    
    # Initialize a list to store the Fibonacci sequence
    fibonacci_sequence = [1, 1]
    
    # Loop through the roads and add the heights of the mansions connected by each road to the Fibonacci sequence
    for road in roads:
        mansion1 = mansion_indices[road[0]]
        mansion2 = mansion_indices[road[1]]
        height1 = mansion_heights[mansion1]
        height2 = mansion_heights[mansion2]
        if height1 > height2:
            fibonacci_sequence.append(height1 + height2)
        else:
            fibonacci_sequence.append(height2 + height1)
    
    # Sort the Fibonacci sequence in descending order
    fibonacci_sequence.sort(reverse=True)
    
    # Initialize a variable to store the length of the longest Fibonacci Tour
    longest_tour = 0
    
    # Loop through the Fibonacci sequence and check if it is a valid Fibonacci Tour
    for i in range(len(fibonacci_sequence)):
        current_sequence = fibonacci_sequence[:i+1]
        if is_fibonacci_tour(current_sequence, mansion_heights, roads):
            longest_tour = max(longest_tour, len(current_sequence))
    
    return longest_tour

def is_fibonacci_tour(fibonacci_sequence, mansion_heights, roads):
    # Check if the Fibonacci sequence is a valid Fibonacci sequence
    if fibonacci_sequence[0] != 1 or fibonacci_sequence[-1] != 1:
        return False
    
    # Loop through the Fibonacci sequence and check if it is a valid Fibonacci Tour
    for i in range(len(fibonacci_sequence)-1):
        current_height = fibonacci_sequence[i]
        next_height = fibonacci_sequence[i+1]
        if current_height + next_height not in mansion_heights.values():
            return False
        if (current_height, next_height) not in roads and (next_height, current_height) not in roads:
            return False
    
    return True

def main():
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))
    roads = []
    for _ in range(m):
        a, b = map(int, input().split())
        roads.append((a, b))
    print(get_fibonacci_tour(n, m, heights, roads))

if __name__ == "__main__":
    main()

