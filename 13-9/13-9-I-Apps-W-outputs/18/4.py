
def get_max_minutes(a1, a2):
    minutes = 0
    while a1 > 0 and a2 > 0:
        if a1 <= 100:
            a2 -= 2
        else:
            a1 -= 1
        a1 = min(a1 + 1, 100)
        a2 = min(a2 + 1, 100)
        minutes += 1
    return minutes

def main():
    a1, a2 = map(int, input().split())
    print(get_max_minutes(a1, a2))

if __name__ == '__main__':
    main()

