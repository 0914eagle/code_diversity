
def get_codecraft_t_shirt_winners(s):
    i = (s // 50) % 475
    winners = []
    for _ in range(25):
        i = (i * 96 + 42) % 475
        winners.append(26 + i)
    return winners

def get_number_of_successful_hacks(x, y, p):
    winners = get_codecraft_t_shirt_winners(x)
    if p in winners:
        return 0
    else:
        return min(25, (y - x) // 100)

if __name__ == '__main__':
    p, x, y = map(int, input().split())
    print(get_number_of_successful_hacks(x, y, p))

