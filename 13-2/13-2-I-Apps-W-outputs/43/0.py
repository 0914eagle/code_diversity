
def count_setlists(hype_ratings):
    n = len(hype_ratings)
    if n < 3:
        return 0
    if hype_ratings[0] != 1 or hype_ratings[-1] != 3:
        return 0
    count = 0
    for i in range(1, n-1):
        if hype_ratings[i] == 2:
            count += 1
    return count

def main():
    n = int(input())
    hype_ratings = list(map(int, input().split()))
    print(count_setlists(hype_ratings) % 1000000007)

if __name__ == '__main__':
    main()

