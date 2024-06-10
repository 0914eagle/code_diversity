
def get_solution(a_00, a_01, a_10, a_11):
    if a_00 + a_01 + a_10 + a_11 == 0:
        return "Impossible"
    
    s = ""
    while a_00 > 0 or a_01 > 0 or a_10 > 0 or a_11 > 0:
        if a_00 > 0 and a_01 > 0:
            s += "01"
            a_00 -= 1
            a_01 -= 1
        elif a_00 > 0 and a_10 > 0:
            s += "00"
            a_00 -= 1
            a_10 -= 1
        elif a_01 > 0 and a_11 > 0:
            s += "10"
            a_01 -= 1
            a_11 -= 1
        elif a_00 > 0 and a_11 > 0:
            s += "01"
            a_00 -= 1
            a_11 -= 1
        elif a_01 > 0 and a_10 > 0:
            s += "10"
            a_01 -= 1
            a_10 -= 1
        elif a_00 > 0:
            s += "0"
            a_00 -= 1
        elif a_01 > 0:
            s += "1"
            a_01 -= 1
        elif a_10 > 0:
            s += "0"
            a_10 -= 1
        elif a_11 > 0:
            s += "1"
            a_11 -= 1
    
    return s

def main():
    a_00, a_01, a_10, a_11 = map(int, input().split())
    print(get_solution(a_00, a_01, a_10, a_11))

if __name__ == '__main__':
    main()

