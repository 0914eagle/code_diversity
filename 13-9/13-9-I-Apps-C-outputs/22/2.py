
def solve(a_00, a_01, a_10, a_11):
    if a_00 + a_01 + a_10 + a_11 == 0:
        return "Impossible"
    
    s = ""
    while a_00 + a_01 + a_10 + a_11 > 0:
        if a_00 > 0:
            s += "00"
            a_00 -= 1
        elif a_01 > 0:
            s += "01"
            a_01 -= 1
        elif a_10 > 0:
            s += "10"
            a_10 -= 1
        elif a_11 > 0:
            s += "11"
            a_11 -= 1
    
    return s

def main():
    a_00, a_01, a_10, a_11 = map(int, input().split())
    print(solve(a_00, a_01, a_10, a_11))

if __name__ == '__main__':
    main()

