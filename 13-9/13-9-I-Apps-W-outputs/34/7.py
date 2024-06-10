
def get_teammate(n, strengths):
    # Initialize a dictionary to store the teammate for each person
    teammates = {}
    
    # Iterate through the strengths of each possible combination of two people
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If the strength of the team is the highest among all possible teams,
            # set the teammate for person i and j
            if strengths[i - 1][j - 1] == max(strengths[i - 1]):
                teammates[i] = j
                teammates[j] = i
    
    # Return the teammate for each person
    return teammates

def main():
    # Read the input
    n = int(input())
    strengths = []
    for i in range(n):
        strengths.append(list(map(int, input().split())))
    
    # Get the teammate for each person
    teammates = get_teammate(n, strengths)
    
    # Print the teammate for each person
    for i in range(1, n + 1):
        print(teammates[i], end=" ")

if __name__ == '__main__':
    main()

