
def get_max_emeralds(sticks, diamonds):
    # Initialize variables
    shovels = 0
    swords = 0
    emeralds = 0

    # Craft shovels
    while sticks >= 2 and diamonds >= 1:
        sticks -= 2
        diamonds -= 1
        shovels += 1

    # Craft swords
    while diamonds >= 2 and sticks >= 1:
        diamonds -= 2
        sticks -= 1
        swords += 1

    # Calculate emeralds
    emeralds = shovels + swords

    return emeralds

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        sticks, diamonds = map(int, input().split())
        emeralds = get_max_emeralds(sticks, diamonds)
        print(emeralds)

if __name__ == '__main__':
    main()

