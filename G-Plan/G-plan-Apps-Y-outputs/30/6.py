
def count_slimes(N, S):
    slimes = {}
    count = 0
    for color in S:
        if color not in slimes or slimes[color] == 0:
            count += 1
            slimes[color] = 1
        else:
            slimes[color] = 0
    return count

if __name__ == "__main__":
    N = int(input())
    S = input().strip()
    result = count_slimes(N, S)
    print(result)
