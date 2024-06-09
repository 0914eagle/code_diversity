
def get_max_emeralds(a, b):
    # Initialize variables
    sticks = a
    diamonds = b
    emeralds = 0

    # Craft as many swords as possible
    num_swords = min(diamonds // 2, sticks)
    emeralds += num_swords
    sticks -= num_swords
    diamonds -= 2 * num_swords

    # Craft as many shovels as possible
    num_shovels = min(sticks // 2, diamonds)
    emeralds += num_shovels
    diamonds -= num_shovels
    sticks -= 2 * num_shovels

    return emeralds

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        a, b = map(int, input().split())
        print(get_max_emeralds(a, b))

if __name__ == '__main__':
    main()

