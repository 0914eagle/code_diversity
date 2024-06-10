
def solve(s):
    # Initialize variables
    like = True
    positions = []
    
    # Check if the string contains "one" or "two"
    if "one" in s or "two" in s:
        like = False
    
    # Check if the string contains "oneone" or "two"
    for i in range(len(s) - 1):
        if s[i:i+2] == "on" or s[i:i+2] == "tw":
            like = False
            positions.append(i)
    
    # Return the result
    if like:
        return 0, []
    else:
        return len(positions), positions

def main():
    # Read the input
    t = int(input())
    strings = []
    for i in range(t):
        strings.append(input())
    
    # Solve the problem
    results = []
    for string in strings:
        results.append(solve(string))
    
    # Print the results
    for result in results:
        print(result[0])
        for position in result[1]:
            print(position, end=" ")
        print()

if __name__ == '__main__':
    main()

