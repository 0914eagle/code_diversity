
def get_remainders(x, k, ancient_numbers):
    remainders = []
    for ancient_number in ancient_numbers:
        remainders.append(x % ancient_number)
    return remainders

def has_winning_strategy(k, ancient_numbers):
    if k in ancient_numbers:
        return True
    for i in range(len(ancient_numbers)):
        for j in range(i+1, len(ancient_numbers)):
            if ancient_numbers[i] % ancient_numbers[j] == 0:
                return False
    return True

def main():
    n, k = map(int, input().split())
    ancient_numbers = list(map(int, input().split()))
    print("Yes") if has_winning_strategy(k, ancient_numbers) else print("No")

if __name__ == '__main__':
    main()

