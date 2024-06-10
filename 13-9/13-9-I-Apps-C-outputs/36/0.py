
def is_winning_strategy(k, ancient_values):
    # Check if k is in the list of ancient values
    if k in ancient_values:
        return True
    
    # Check if any of the ancient values is a factor of k
    for a in ancient_values:
        if k % a == 0:
            return True
    
    # Check if any of the ancient values is a factor of any of the other ancient values
    for i in range(len(ancient_values)):
        for j in range(i+1, len(ancient_values)):
            if ancient_values[i] % ancient_values[j] == 0:
                return True
    
    # If none of the above conditions are met, then Arya has no winning strategy
    return False

def main():
    n, k = map(int, input().split())
    ancient_values = list(map(int, input().split()))
    print("Yes") if is_winning_strategy(k, ancient_values) else print("No")

if __name__ == '__main__':
    main()

