
def get_disliked_digits(disliked_digits):
    return set(map(int, disliked_digits))

def get_min_amount(total, disliked_digits):
    min_amount = total
    for i in range(1, total + 1):
        if all(str(i)[j] not in disliked_digits for j in range(len(str(i)))):
            min_amount = min(min_amount, i)
    return min_amount

def main():
    total, num_disliked_digits = map(int, input().split())
    disliked_digits = get_disliked_digits(input().split())
    print(get_min_amount(total, disliked_digits))

if __name__ == '__main__':
    main()

