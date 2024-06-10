
def is_reachable(n, k, line):
    start, end = line.index('G'), line.index('T')
    if abs(start - end) <= k:
        return True
    for i in range(start, end):
        if line[i] == '#':
            return False
    return True

def main():
    n, k = map(int, input().split())
    line = input()
    if is_reachable(n, k, line):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

