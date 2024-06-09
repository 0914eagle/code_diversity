
def get_mentor_counts(skills, pairs_in_quarrel):
    # Initialize a dictionary to store the count of mentors for each programmer
    mentor_counts = {}
    for i in range(len(skills)):
        mentor_counts[i] = 0
    
    # Iterate over the pairs of programmers in quarrel
    for pair in pairs_in_quarrel:
        # Get the indices of the programmers in the pair
        i, j = pair
        
        # If the skill of the first programmer is greater than the skill of the second programmer
        if skills[i] > skills[j]:
            # Increment the count of mentors for the second programmer
            mentor_counts[j] += 1
    
    return mentor_counts

def main():
    # Read the number of programmers and the number of pairs of programmers in quarrel
    n, k = map(int, input().split())
    
    # Read the skills of each programmer
    skills = list(map(int, input().split()))
    
    # Read the pairs of programmers in quarrel
    pairs_in_quarrel = []
    for _ in range(k):
        pair = list(map(int, input().split()))
        pairs_in_quarrel.append(pair)
    
    # Get the count of mentors for each programmer
    mentor_counts = get_mentor_counts(skills, pairs_in_quarrel)
    
    # Print the count of mentors for each programmer
    for i in range(n):
        print(mentor_counts[i], end=" ")

if __name__ == '__main__':
    main()

