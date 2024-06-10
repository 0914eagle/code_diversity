
def is_winning_strategy(k, c):
    # Check if k is a multiple of any of the ancient numbers
    for i in range(len(c)):
        if k % c[i] == 0:
            return True
    
    # Check if there exists an ancient number that is a multiple of k
    for i in range(len(c)):
        if c[i] % k == 0:
            return False
    
    # If no multiple exists, then Arya can't be sure what the remainder is
    return False

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    print("Yes") if is_winning_strategy(k, c) else print("No")

if __name__ == '__main__':
    main()

