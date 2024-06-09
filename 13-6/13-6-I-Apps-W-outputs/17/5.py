
def get_t_shirt_winners(s):
    i = (s // 50) % 475
    winners = []
    for _ in range(25):
        i = (i * 96 + 42) % 475
        winners.append(26 + i)
    return winners

def get_hacks_needed(p, x, y):
    t_shirt_winners = get_t_shirt_winners(x)
    hacks_needed = 0
    for i in range(len(t_shirt_winners)):
        if t_shirt_winners[i] == p:
            return hacks_needed
        if t_shirt_winners[i] > p:
            hacks_needed += 1
    return hacks_needed + (x - y) // 100

def main():
    p, x, y = map(int, input().split())
    print(get_hacks_needed(p, x, y))

if __name__ == '__main__':
    main()

