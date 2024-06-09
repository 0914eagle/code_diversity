
def get_t_shirt_winners(s):
    i = (s // 50) % 475
    t_shirt_winners = []
    for _ in range(25):
        i = (i * 96 + 42) % 475
        t_shirt_winners.append(26 + i)
    return t_shirt_winners

def get_min_hacks(p, x, y):
    t_shirt_winners = get_t_shirt_winners(x)
    min_hacks = 0
    for t_shirt_winner in t_shirt_winners:
        if t_shirt_winner > p:
            min_hacks += 1
        elif t_shirt_winner == p:
            break
    return min_hacks

def main():
    p, x, y = map(int, input().split())
    print(get_min_hacks(p, x, y))

if __name__ == '__main__':
    main()

