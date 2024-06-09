
def get_codecraft_t_shirt_winners(s):
    i = (s // 50) % 475
    winners = []
    for _ in range(25):
        i = (i * 96 + 42) % 475
        winners.append(26 + i)
    return winners

def get_minimum_hacks(p, x, y):
    codecraft_t_shirt_winners = get_codecraft_t_shirt_winners(x)
    if p in codecraft_t_shirt_winners:
        return 0
    else:
        hacks = 0
        while x < y:
            x += 100
            hacks += 1
        return hacks

if __name__ == '__main__':
    p, x, y = map(int, input().split())
    print(get_minimum_hacks(p, x, y))

