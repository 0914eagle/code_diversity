
def get_paint_required(a):
    return sum(a)

def get_maximum_number(v, a):
    max_num = -1
    for i in range(1, 10):
        if v >= get_paint_required(a[:i]):
            max_num = i
            v -= get_paint_required(a[:i])
        else:
            break
    return max_num

def main():
    v = int(input())
    a = list(map(int, input().split()))
    print(get_maximum_number(v, a))

if __name__ == '__main__':
    main()

