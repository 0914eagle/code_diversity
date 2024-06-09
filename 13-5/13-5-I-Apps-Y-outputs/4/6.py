
def f1(n, k, r, pairs):
    # Initialize a dictionary to store the mentor count for each programmer
    mentor_count = {}
    for i in range(n):
        mentor_count[i] = 0
    
    # Iterate over the pairs of programmers in a quarrel
    for pair in pairs:
        # Get the indices of the programmers in the pair
        x, y = pair
        
        # Increment the mentor count for the programmer with the higher skill
        if r[x] > r[y]:
            mentor_count[x] += 1
        else:
            mentor_count[y] += 1
    
    return [mentor_count[i] for i in range(n)]

def f2(n, k, r, pairs):
    # Initialize a dictionary to store the mentor count for each programmer
    mentor_count = {}
    for i in range(n):
        mentor_count[i] = 0
    
    # Iterate over the pairs of programmers in a quarrel
    for pair in pairs:
        # Get the indices of the programmers in the pair
        x, y = pair
        
        # Increment the mentor count for the programmer with the higher skill
        if r[x] > r[y]:
            mentor_count[x] += 1
        else:
            mentor_count[y] += 1
    
    return [mentor_count[i] for i in range(n)]

if __name__ == '__main__':
    n, k = map(int, input().split())
    r = list(map(int, input().split()))
    pairs = []
    for _ in range(k):
        x, y = map(int, input().split())
        pairs.append((x, y))
    
    print(f1(n, k, r, pairs))
    print(f2(n, k, r, pairs))

