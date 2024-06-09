
def solve(n, swimmers):
    # Sort the swimmers by their x coordinate
    swimmers.sort(key=lambda x: x[0])

    # Initialize the positions of you and your coworker
    you = [0, 0]
    coworker = [0, 0]

    # Divide the swimmers into two groups
    group1 = swimmers[:n//2]
    group2 = swimmers[n//2:]

    # Find the midpoint between the two groups
    midpoint = (sum([s[0] for s in group1]) + sum([s[0] for s in group2])) // (n//2)

    # Move you and your coworker to the midpoint
    you[0] = midpoint
    coworker[0] = midpoint

    # Print the positions of you and your coworker
    print(you)
    print(coworker)

# Main function
if __name__ == "__main__":
    # Read the input
    n = int(input())
    swimmers = []
    for i in range(n):
        x, y = map(int, input().split())
        swimmers.append([x, y])

    # Solve the problem
    solve(n, swimmers)

