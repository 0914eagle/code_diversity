
def get_disliked_digits():
    return set(map(int, input().split()))

def get_min_amount(disliked_digits, total):
    min_amount = total
    for i in range(1, total+1):
        if all(str(i) not in disliked_digits for i in str(i)):
            min_amount = min(min_amount, i)
    return min_amount

def main():
    total, k = map(int, input().split())
    disliked_digits = get_disliked_digits()
    print(get_min_amount(disliked_digits, total))

if __name__ == '__main__':
    main()

