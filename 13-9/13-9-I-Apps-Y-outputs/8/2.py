
def can_start_round_dance(p):
    n = len(p)
    if n == 1:
        return "YES"
    if n == 2:
        if p[0] == 1 and p[1] == 2:
            return "YES"
        else:
            return "NO"
    if n == 3:
        if p[0] == 1 and p[1] == 2 and p[2] == 3:
            return "YES"
        else:
            return "NO"
    if n == 4:
        if p[0] == 1 and p[1] == 2 and p[2] == 3 and p[3] == 4:
            return "YES"
        else:
            return "NO"
    if n == 5:
        if p[0] == 1 and p[1] == 2 and p[2] == 3 and p[3] == 4 and p[4] == 5:
            return "YES"
        else:
            return "NO"
    else:
        if p[0] == 1 and p[1] == 2 and p[2] == 3 and p[3] == 4 and p[4] == 5:
            return "YES"
        else:
            return "NO"

def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print(can_start_round_dance(p))

if __name__ == '__main__':
    main()

