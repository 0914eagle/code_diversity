
def get_danger(chemicals, reactions):
    # Initialize the danger as 1
    danger = 1
    
    # Loop through each reaction
    for x, y in reactions:
        # If the chemicals can react, multiply the danger by 2
        if x in chemicals and y in chemicals:
            danger *= 2
    
    return danger

def main():
    # Read the number of chemicals and reactions
    n, m = map(int, input().split())
    
    # Read the reactions
    reactions = []
    for _ in range(m):
        x, y = map(int, input().split())
        reactions.append((x, y))
    
    # Get the maximum possible danger
    danger = get_danger(range(1, n + 1), reactions)
    
    # Print the answer
    print(danger)

if __name__ == '__main__':
    main()

