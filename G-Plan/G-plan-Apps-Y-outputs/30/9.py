
def count_slimes(N, S):
    slimes = {}
    count = 0
    for i in range(N):
        if i == 0 or S[i] != S[i-1]:
            count += 1
    return count

if __name__ == "__main__":
    N = int(input())
    S = input().strip()
    result = count_slimes(N, S)
    print(result)
