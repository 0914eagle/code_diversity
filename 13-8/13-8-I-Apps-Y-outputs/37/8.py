
def get_disliked_digits(k):
    disliked_digits = []
    for i in range(1, 10):
        if i not in range(1, k+1):
            disliked_digits.append(i)
    return disliked_digits

def get_min_amount(n, disliked_digits):
    min_amount = 0
    while min_amount < n:
        min_amount += 1
        if all(str(min_amount)[i] not in disliked_digits for i in range(len(str(min_amount)))):
            return min_amount
    return min_amount

def main():
    n, k = map(int, input().split())
    disliked_digits = get_disliked_digits(k)
    print(get_min_amount(n, disliked_digits))

if __name__ == '__main__':
    main()

