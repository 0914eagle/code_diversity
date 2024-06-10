
def is_takahashi_correct(c):
    a_set = set()
    b_set = set()
    for i in range(3):
        for j in range(3):
            a_set.add(c[i][j] - b[j])
            b_set.add(c[i][j] - a[i])
    return len(a_set) == 6 and len(b_set) == 6

def main():
    c = []
    for i in range(3):
        c.append(list(map(int, input().split())))
    print("Yes" if is_takahashi_correct(c) else "No")

if __name__ == '__main__':
    main()

