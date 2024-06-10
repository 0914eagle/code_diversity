
def get_party_day(n, trees):
    # Sort the tree growth days in ascending order
    trees.sort()
    
    # Initialize the party day as the last tree growth day
    party_day = trees[-1]
    
    # Loop through the trees in reverse order
    for i in range(n-1, 0, -1):
        # Calculate the day when the current tree will be ready
        tree_day = party_day + trees[i-1]
        
        # If the current tree day is earlier than the current party day, update the party day
        if tree_day < party_day:
            party_day = tree_day
    
    return party_day

def main():
    n = int(input())
    trees = list(map(int, input().split()))
    print(get_party_day(n, trees))

if __name__ == '__main__':
    main()

