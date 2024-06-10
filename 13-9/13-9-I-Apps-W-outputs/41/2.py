
def read_input():
    n, t = map(int, input().split())
    segments = []
    for _ in range(n):
        d, s = map(int, input().split())
        segments.append((d, s))
    return n, t, segments

def compute_c(segments):
    c = 0
    for d, s in segments:
        c += d * s
    return c / sum(d for d, s in segments)

def main():
    n, t, segments = read_input()
    c = compute_c(segments)
    print(c)

if __name__ == '__main__':
    main()

