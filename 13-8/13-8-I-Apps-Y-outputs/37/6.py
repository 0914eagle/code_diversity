
def is_disliked(n, disliked_digits):
    while n > 0:
        if str(n % 10) in disliked_digits:
            return True
        n //= 10
    return False

def solve(n, disliked_digits):
    min_amount = 1
    while min_amount <= n:
        if not is_disliked(min_amount, disliked_digits):
            return min_amount
        min_amount += 1
    return -1

def main():
    n, k = map(int, input().split())
    disliked_digits = set(map(int, input().split()))
    print(solve(n, disliked_digits))

if __name__ == '__main__':
    main()

