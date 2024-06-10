
def get_max_openable_chests(chests, keys):
    max_openable_chests = 0
    for key in keys:
        for chest in chests:
            if (chest + key) % 2 == 1:
                max_openable_chests += 1
                break
    return max_openable_chests

def main():
    n, m = map(int, input().split())
    chests = list(map(int, input().split()))
    keys = list(map(int, input().split()))
    print(get_max_openable_chests(chests, keys))

if __name__ == '__main__':
    main()

