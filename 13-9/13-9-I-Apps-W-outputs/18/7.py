
def get_max_minutes(a1, a2):
    if a1 == 0 or a2 == 0:
        return 0
    
    minutes = 0
    while a1 > 0 and a2 > 0:
        if a1 <= 100:
            a1 = 100
        if a2 <= 100:
            a2 = 100
        
        a1 -= 2
        a2 -= 2
        if a1 == 0 or a2 == 0:
            break
        
        a1 += 1
        a2 += 1
        minutes += 1
    
    return minutes

def main():
    a1, a2 = map(int, input().split())
    print(get_max_minutes(a1, a2))

if __name__ == '__main__':
    main()

