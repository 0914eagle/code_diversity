
def get_max_minutes(a_1, a_2):
    if a_1 == 0 or a_2 == 0:
        return 0
    
    minutes = 0
    while a_1 > 0 and a_2 > 0:
        if a_1 > a_2:
            a_1 -= 2
        else:
            a_2 -= 2
        minutes += 1
        if a_1 == 0 or a_2 == 0:
            break
    
    return minutes

def main():
    a_1, a_2 = map(int, input().split())
    print(get_max_minutes(a_1, a_2))

if __name__ == '__main__':
    main()

