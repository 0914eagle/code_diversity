
def get_remainder(x, k, ancient_numbers):
    if k in ancient_numbers:
        return x % k
    else:
        return None

def has_winning_strategy(k, ancient_numbers):
    if k in ancient_numbers:
        return True
    else:
        return False

def main():
    n, k = map(int, input().split())
    ancient_numbers = list(map(int, input().split()))
    print("Yes" if has_winning_strategy(k, ancient_numbers) else "No")

if __name__ == '__main__':
    main()

