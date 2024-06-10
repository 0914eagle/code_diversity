
def get_largest_number(paint_liters, paint_needed):
    largest_number = 0
    for i in range(1, 10):
        if paint_needed[i] <= paint_liters:
            largest_number = largest_number * 10 + i
            paint_liters -= paint_needed[i]
        else:
            break
    return largest_number

def get_paint_needed(a):
    paint_needed = [0] * 10
    for i in range(1, 10):
        paint_needed[i] = a[i]
    return paint_needed

def main():
    paint_liters = int(input())
    a = list(map(int, input().split()))
    paint_needed = get_paint_needed(a)
    largest_number = get_largest_number(paint_liters, paint_needed)
    print(largest_number)

if __name__ == '__main__':
    main()

