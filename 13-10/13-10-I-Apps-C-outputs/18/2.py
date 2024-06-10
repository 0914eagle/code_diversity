
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def find_mod_remainders(k, ancient_numbers):
    remainders = set()
    for ancient_number in ancient_numbers:
        remainder = k % ancient_number
        remainders.add(remainder)
    return remainders

def is_winning_strategy(k, ancient_numbers):
    remainders = find_mod_remainders(k, ancient_numbers)
    if len(remainders) == 1:
        return True
    else:
        return False

def main():
    n, k = map(int, input().split())
    ancient_numbers = list(map(int, input().split()))
    if is_winning_strategy(k, ancient_numbers):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

