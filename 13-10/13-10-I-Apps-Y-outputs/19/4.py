
def get_median(s, t):
    k = len(s)
    assert len(t) == k
    assert s < t
    assert (t - s).count(True) % 2 == 1

    mid = (t - s).index(True) // 2
    return "".join(chr(ord('a') + mid) for _ in range(k))

def main():
    k = int(input())
    s = input()
    t = input()
    print(get_median(s, t))

if __name__ == '__main__':
    main()

