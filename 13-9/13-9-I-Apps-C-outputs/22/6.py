
def find_string(a_00, a_01, a_10, a_11):
    if a_00 + a_01 + a_10 + a_11 == 0:
        return "Impossible"
    
    s = ""
    while len(s) < 1000000:
        if a_00 > 0 and a_01 > 0:
            s += "01"
            a_00 -= 1
            a_01 -= 1
        elif a_10 > 0 and a_11 > 0:
            s += "10"
            a_10 -= 1
            a_11 -= 1
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
        else:
            break
    
    if len(s) == 0:
        return "Impossible"
    else:
        return s

def main():
    a_00, a_01, a_10, a_11 = map(int, input().split())
    print(find_string(a_00, a_01, a_10, a_11))

if __name__ == '__main__':
    main()

