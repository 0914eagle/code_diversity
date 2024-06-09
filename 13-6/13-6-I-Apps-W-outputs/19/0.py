
def get_max_fruits(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return 0
    lemons = a
    apples = b
    pears = c
    while lemons > 0 and apples > 0 and pears > 0:
        if lemons % 2 == 0 and apples % 4 == 0 and pears % 4 == 0:
            break
        if lemons % 2 != 0:
            lemons -= 1
        if apples % 4 != 0:
            apples -= 1
        if pears % 4 != 0:
            pears -= 1
    return lemons + apples + pears

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(get_max_fruits(a, b, c))

if __name__ == '__main__':
    main()

