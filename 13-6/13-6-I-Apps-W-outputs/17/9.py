
def get_t_shirt_winners(s):
    i = (s // 50) % 475
    t_shirt_winners = []
    for _ in range(25):
        i = (i * 96 + 42) % 475
        t_shirt_winners.append(26 + i)
    return t_shirt_winners

def get_min_hacks(p, x, y):
    t_shirt_winners = get_t_shirt_winners(x)
    if p in t_shirt_winners:
        return 0
    else:
        min_hacks = float('inf')
        for i in range(25):
            if x + 100 * i >= y:
                min_hacks = min(min_hacks, i)
        return min_hacks

if __name__ == '__main__':
    p, x, y = map(int, input().split())
    print(get_min_hacks(p, x, y))

