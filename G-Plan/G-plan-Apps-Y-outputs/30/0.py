
def count_slimes(N, S):
    slimes = {}
    count = 0
    for color in S:
        if color not in slimes or slimes[color] != count:
            count += 1
            slimes[color] = count
    return count

if __name__ == "__main__":
    N = int(input())
    S = input().strip()
    print(count_slimes(N, S))
