
def get_max_minutes(a_1, a_2):
    minutes = 0
    while a_1 > 0 and a_2 > 0:
        minutes += 1
        a_1 = max(a_1 - 2, 0)
        a_2 = max(a_2 - 2, 0)
        if a_1 == 0:
            a_1 = 100
        if a_2 == 0:
            a_2 = 100
    return minutes

def main():
    a_1, a_2 = map(int, input().split())
    print(get_max_minutes(a_1, a_2))

if __name__ == '__main__':
    main()

