
def check_strategy(k, ancient_values):
    # Check if k is one of the ancient values
    if k in ancient_values:
        return True
    
    # Check if any two ancient values have a common multiple that is also an ancient value
    for i in range(len(ancient_values)):
        for j in range(i+1, len(ancient_values)):
            if ancient_values[i] * ancient_values[j] in ancient_values:
                return True
    
    # If none of the above conditions are met, then Arya has no winning strategy
    return False

def main():
    n, k = map(int, input().split())
    ancient_values = list(map(int, input().split()))
    print("Yes") if check_strategy(k, ancient_values) else print("No")

if __name__ == '__main__':
    main()

