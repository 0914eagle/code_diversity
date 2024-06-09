
def get_t_shirt_places(s):
    i = (s // 50) % 475
    t_shirt_places = []
    for _ in range(25):
        i = (i * 96 + 42) % 475
        t_shirt_places.append(26 + i)
    return t_shirt_places

def get_min_hacks(p, x, y):
    t_shirt_places = get_t_shirt_places(x)
    min_hacks = 0
    for t_shirt_place in t_shirt_places:
        if t_shirt_place > p:
            min_hacks += 1
        elif t_shirt_place == p and x < y:
            min_hacks += 1
    return min_hacks

def main():
    p, x, y = map(int, input().split())
    print(get_min_hacks(p, x, y))

if __name__ == '__main__':
    main()

