
def get_shovels(sticks):
    return sticks // 2

def get_swords(diamonds):
    return diamonds // 2

def get_emeralds(shovels, swords):
    return shovels + swords

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        sticks, diamonds = map(int, input().split())
        shovels = get_shovels(sticks)
        swords = get_swords(diamonds)
        emeralds = get_emeralds(shovels, swords)
        print(emeralds)

if __name__ == '__main__':
    main()

