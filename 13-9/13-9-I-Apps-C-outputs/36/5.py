
def is_winning_strategy(n, k, ancient_values):
    # Check if k is one of the ancient values
    if k in ancient_values:
        return True
    
    # Check if any two ancient values have a common remainder
    for i in range(n):
        for j in range(i+1, n):
            if ancient_values[i] % k == ancient_values[j] % k:
                return False
    
    return True

def main():
    n, k = map(int, input().split())
    ancient_values = list(map(int, input().split()))
    print("Yes") if is_winning_strategy(n, k, ancient_values) else print("No")

if __name__ == '__main__':
    main()

