
def get_mentors(n, r, k, quarrels):
    # Initialize a dictionary to store the mentors for each programmer
    mentors = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the quarrels
    for x, y in quarrels:
        # If the skills of the two programmers in the quarrel are not equal,
        # then the skill of the first programmer is greater than the skill of the second programmer
        if r[x - 1] > r[y - 1]:
            # Increment the mentor count for the first programmer
            mentors[x] += 1
    
    # Return the list of mentors
    return [mentors[i] for i in range(1, n + 1)]

def main():
    # Read the input
    n, k = map(int, input().split())
    r = list(map(int, input().split()))
    quarrels = []
    for _ in range(k):
        x, y = map(int, input().split())
        quarrels.append((x, y))
    
    # Call the function to get the mentors
    mentors = get_mentors(n, r, k, quarrels)
    
    # Print the mentors
    print(*mentors, sep='\n')

if __name__ == '__main__':
    main()

