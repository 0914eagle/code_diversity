
def get_max_emeralds(a, b):
    # Initialize variables
    emeralds = 0
    sticks = a
    diamonds = b

    # Craft as many shovels as possible
    while sticks >= 2 and diamonds >= 1:
        sticks -= 2
        diamonds -= 1
        emeralds += 1

    # Craft as many swords as possible
    while diamonds >= 2 and sticks >= 1:
        diamonds -= 2
        sticks -= 1
        emeralds += 1

    return emeralds

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        a, b = map(int, input().split())
        print(get_max_emeralds(a, b))

if __name__ == '__main__':
    main()

