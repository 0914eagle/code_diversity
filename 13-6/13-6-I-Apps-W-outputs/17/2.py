
def get_codecraft_winners(s):
    i = (s // 50) % 475
    winners = []
    for _ in range(25):
        i = (i * 96 + 42) % 475
        winners.append(26 + i)
    return winners

def get_min_hacks(p, x, y):
    codecraft_winners = get_codecraft_winners(x)
    if p in codecraft_winners:
        return 0
    else:
        min_hacks = 10000
        for i in range(25):
            if x + (i + 1) * 100 <= y:
                min_hacks = min(min_hacks, i)
        return min_hacks

if __name__ == '__main__':
    p, x, y = map(int, input().split())
    print(get_min_hacks(p, x, y))

