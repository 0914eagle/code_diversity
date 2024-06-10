
def get_heights():
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
    return N, K, heights

def count_tall_friends(N, K, heights):
    count = 0
    for h in heights:
        if h >= K:
            count += 1
    return count

def main():
    N, K, heights = get_heights()
    print(count_tall_friends(N, K, heights))

if __name__ == '__main__':
    main()

