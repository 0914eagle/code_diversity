
def read_input():
    n = int(input())
    cs = list(map(int, input().split()))
    return n, cs

def is_possible(cs):
    if len(cs) == 1:
        return True
    if len(cs) == 2:
        return cs[0] + cs[1] == 2
    if len(cs) == 3:
        return cs[0] + cs[1] + cs[2] == 3
    if len(cs) == 4:
        return cs[0] + cs[1] + cs[2] + cs[3] == 4
    return any(cs[i] + cs[i+1] + cs[i+2] + cs[i+3] == 4 for i in range(len(cs)-3))

def main():
    n, cs = read_input()
    print("YES") if is_possible(cs) else print("NO")

if __name__ == '__main__':
    main()

