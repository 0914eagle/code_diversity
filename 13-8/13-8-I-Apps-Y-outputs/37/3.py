
def get_disliked_digits(disliked_digits):
    return set(disliked_digits)

def get_min_amount(total, disliked_digits):
    min_amount = total
    for i in range(1, total+1):
        if all(str(i) not in disliked_digits for disliked_digit in disliked_digits):
            min_amount = i
            break
    return min_amount

def main():
    total, num_disliked_digits = map(int, input().split())
    disliked_digits = list(map(int, input().split()))
    disliked_digits = get_disliked_digits(disliked_digits)
    min_amount = get_min_amount(total, disliked_digits)
    print(min_amount)

if __name__ == '__main__':
    main()

