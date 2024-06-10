
def can_start_round_dance(permutation):
    # Check if the permutation is a circular permutation
    if permutation == list(range(1, len(permutation) + 1)):
        return "YES"
    
    # Check if the permutation is a reverse circular permutation
    if permutation == list(range(len(permutation), 0, -1)):
        return "YES"
    
    # Check if the permutation is a circular shift of a circular permutation
    for i in range(1, len(permutation)):
        if permutation[i:] + permutation[:i] == list(range(1, len(permutation) + 1)):
            return "YES"
    
    # Check if the permutation is a reverse circular shift of a circular permutation
    for i in range(1, len(permutation)):
        if permutation[i:] + permutation[:i] == list(range(len(permutation), 0, -1)):
            return "YES"
    
    # If none of the above conditions are met, return "NO"
    return "NO"

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        permutation = list(map(int, input().split()))
        print(can_start_round_dance(permutation))

if __name__ == '__main__':
    main()

