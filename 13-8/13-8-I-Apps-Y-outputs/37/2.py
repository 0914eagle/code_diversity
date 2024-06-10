
def get_disliked_digits(k):
    return [int(input()) for _ in range(k)]

def get_minimum_amount(n, disliked_digits):
    minimum_amount = 0
    for i in range(1, n+1):
        if all(str(i)[j] not in disliked_digits for j in range(len(str(i))):
            minimum_amount = i
            break
    return minimum_amount

def main():
    n, k = map(int, input().split())
    disliked_digits = get_disliked_digits(k)
    minimum_amount = get_minimum_amount(n, disliked_digits)
    print(minimum_amount)

if __name__ == '__main__':
    main()

