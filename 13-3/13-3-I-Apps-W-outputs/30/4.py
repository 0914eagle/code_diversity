
def count_pairs(N):
    count = 0
    for u in range(N+1):
        for v in range(N+1):
            if u ^ v == u + v:
                count += 1
    return count % 1000000007

if __name__ == '__main__':
    N = int(input())
    print(count_pairs(N))

