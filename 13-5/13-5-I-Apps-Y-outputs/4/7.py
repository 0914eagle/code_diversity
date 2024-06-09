
def get_mentors(n, skills, quarrels):
    # Initialize a dictionary to store the mentors for each programmer
    mentors = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the quarrels
    for x, y in quarrels:
        # If the skills of the two programmers are not in descending order, swap them
        if skills[x - 1] < skills[y - 1]:
            x, y = y, x
        # Increment the mentor count for the stronger programmer
        mentors[x] += 1
    
    return [mentors[i] for i in range(1, n + 1)]

def main():
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))
    quarrels = [tuple(map(int, input().split())) for _ in range(k)]
    print(*get_mentors(n, skills, quarrels))

if __name__ == '__main__':
    main()

