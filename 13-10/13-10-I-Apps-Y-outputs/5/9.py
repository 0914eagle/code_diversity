
def get_input():
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
    return N, K, heights

def solve(N, K, heights):
    count = 0
    for height in heights:
        if height >= K:
            count += 1
    return count

def main():
    N, K, heights = get_input()
    print(solve(N, K, heights))

if __name__ == '__main__':
    main()

