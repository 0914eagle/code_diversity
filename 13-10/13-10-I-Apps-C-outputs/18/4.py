
def is_winning_strategy(n, k, ancient_numbers):
    # Check if k is an ancient number
    if k in ancient_numbers:
        return True
    
    # Check if any pair of ancient numbers has a common remainder
    for i in range(n):
        for j in range(i+1, n):
            if ancient_numbers[i] % k == ancient_numbers[j] % k:
                return True
    
    return False

def main():
    n, k = map(int, input().split())
    ancient_numbers = list(map(int, input().split()))
    print("Yes") if is_winning_strategy(n, k, ancient_numbers) else print("No")

if __name__ == '__main__':
    main()

