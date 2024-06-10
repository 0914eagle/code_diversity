
def get_disliked_digits(input_string):
    disliked_digits = set()
    for digit in input_string:
        if digit != '0' and digit != '2':
            disliked_digits.add(digit)
    return disliked_digits

def get_min_amount(N, disliked_digits):
    min_amount = 0
    while min_amount < N:
        min_amount += 1
        if all(str(min_amount)[i] in disliked_digits for i in range(len(str(min_amount)))):
            break
    return min_amount

def main():
    N, K = map(int, input().split())
    disliked_digits = get_disliked_digits(input())
    min_amount = get_min_amount(N, disliked_digits)
    print(min_amount)

if __name__ == '__main__':
    main()

