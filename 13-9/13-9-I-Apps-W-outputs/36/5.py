
def solve(n, s, t, p):
    # Initialize a dictionary to keep track of the position of the marble
    marble_pos = {i: i for i in range(1, n+1)}
    marble_pos[s] = t
    
    # Initialize a list to keep track of the shuffling operations
    shuffles = []
    
    # Loop through the shuffling operations and apply them to the marble position
    for i in range(len(p)):
        pos = p[i]
        marble_pos[pos] = marble_pos[pos-1]
        shuffles.append(pos)
    
    # Check if the marble has reached its final position
    if marble_pos[t] == t:
        return len(shuffles)
    else:
        return -1

def main():
    n, s, t = map(int, input().split())
    p = list(map(int, input().split()))
    print(solve(n, s, t, p))

if __name__ == '__main__':
    main()

