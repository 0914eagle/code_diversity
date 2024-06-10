
def find_remainder(k, ancient_numbers, x):
    for ancient_number in ancient_numbers:
        if x % ancient_number == k % ancient_number:
            return x % k
    return -1

def main():
    n, k = map(int, input().split())
    ancient_numbers = list(map(int, input().split()))
    x = find_remainder(k, ancient_numbers, x)
    if x != -1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

