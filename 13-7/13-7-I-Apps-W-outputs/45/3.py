
def get_snowball_weight(w, h, u1, d1, u2, d2):
    snowball_weight = w
    current_height = h
    while current_height > 0:
        snowball_weight += current_height
        if current_height == d1 or current_height == d2:
            if snowball_weight - u1 > 0:
                snowball_weight -= u1
            if snowball_weight - u2 > 0:
                snowball_weight -= u2
        current_height -= 1
    return snowball_weight

def main():
    w, h = map(int, input().split())
    u1, d1 = map(int, input().split())
    u2, d2 = map(int, input().split())
    print(get_snowball_weight(w, h, u1, d1, u2, d2))

if __name__ == '__main__':
    main()

