
def get_paint_required(a):
    return sum(a)

def get_max_number(v, a):
    max_number = ""
    for i in range(1, 10):
        if get_paint_required(a[i:]) <= v:
            max_number += str(i)
            v -= get_paint_required(a[i:])
        if v == 0:
            break
    return max_number if max_number != "" else -1

def main():
    v = int(input())
    a = list(map(int, input().split()))
    print(get_max_number(v, a))

if __name__ == '__main__':
    main()

