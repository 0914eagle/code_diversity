
def get_shovels(sticks):
    return sticks // 2

def get_swords(diamonds):
    return diamonds // 2

def get_emeralds(shovels, swords):
    return shovels + swords

def solve(a, b):
    shovels = get_shovels(a)
    swords = get_swords(b)
    emeralds = get_emeralds(shovels, swords)
    return emeralds

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(solve(a, b))

