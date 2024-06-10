
def get_possible_options(n, x, y, z, a):
    # Initialize variables
    options = 0
    visited = [False] * n
    queue = [(0, 0)]
    
    # Loop through the queue
    while queue:
        # Get the current castle and the type of attack
        castle, attack_type = queue.pop(0)
        
        # Check if the castle has at least one defender
        if a[castle] > 0:
            # Check if the attack type is valid
            if attack_type == 0:
                # Mixed attack
                options += 1
            elif attack_type == 1:
                # Infantry attack
                if a[castle] >= y:
                    options += 1
            elif attack_type == 2:
                # Cavalry attack
                if a[castle] >= z:
                    options += 1
                
            # Add the neighbors to the queue
            for neighbor in range(n):
                if not visited[neighbor]:
                    queue.append((neighbor, (attack_type + 1) % 3))
                    
            # Mark the current castle as visited
            visited[castle] = True
    
    # Return the number of possible options
    return options

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        n, x, y, z = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Get the possible options for the first attack
        options = get_possible_options(n, x, y, z, a)
        
        # Print the answer
        print(options)

if __name__ == '__main__':
    main()

