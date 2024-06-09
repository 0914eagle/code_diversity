
def get_mentors(n, r, k, pairs):
    mentors = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if r[i] > r[j] and (i, j) not in pairs and (j, i) not in pairs:
                mentors[i] += 1
                mentors[j] += 1
    return mentors

def main():
    n, k = map(int, input().split())
    r = list(map(int, input().split()))
    pairs = []
    for _ in range(k):
        x, y = map(int, input().split())
        pairs.append((x, y))
    mentors = get_mentors(n, r, k, pairs)
    print(*mentors, sep='\n')

if __name__ == '__main__':
    main()

