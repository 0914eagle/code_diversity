
def is_winning_strategy(n, k, ancient_values):
    # Check if k is one of the ancient values
    if k in ancient_values:
        return True
    
    # Check if there is any value that is a multiple of k and is not one of the ancient values
    for i in range(1, k):
        if i % k == 0 and i not in ancient_values:
            return False
    
    return True

def main():
    n, k = map(int, input().split())
    ancient_values = list(map(int, input().split()))
    print("Yes") if is_winning_strategy(n, k, ancient_values) else print("No")

if __name__ == '__main__':
    main()

