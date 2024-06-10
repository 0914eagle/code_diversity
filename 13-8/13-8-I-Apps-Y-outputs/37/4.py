
def get_disliked_digits(disliked_digits):
    return set(map(int, disliked_digits))

def get_minimum_amount(total, disliked_digits):
    minimum_amount = total
    for i in range(1, total + 1):
        if all(map(lambda x: str(x) not in str(i), disliked_digits)):
            minimum_amount = min(minimum_amount, i)
    return minimum_amount

def main():
    total, num_disliked_digits = map(int, input().split())
    disliked_digits = get_disliked_digits(input().split())
    print(get_minimum_amount(total, disliked_digits))

if __name__ == '__main__':
    main()

