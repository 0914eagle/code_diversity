
def get_prettiness(a, n):
    # Calculate the maximum possible total prettiness of the contest composed of at most three problems
    return max(a[0] + a[1] + a[2], a[0] + a[1] + a[3], a[1] + a[2] + a[3], a[0] + a[2] + a[3])

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_prettiness(a, n))

if __name__ == '__main__':
    main()

