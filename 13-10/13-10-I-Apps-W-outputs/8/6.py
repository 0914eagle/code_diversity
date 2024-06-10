
def get_largest_multiple_of_90(cards):
    multiples_of_90 = []
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            multiple = int(cards[i] + cards[j])
            if multiple % 90 == 0 and multiple not in multiples_of_90:
                multiples_of_90.append(multiple)
    if len(multiples_of_90) == 0:
        return -1
    return max(multiples_of_90)

def main():
    n = int(input())
    cards = input().split()
    print(get_largest_multiple_of_90(cards))

if __name__ == '__main__':
    main()

