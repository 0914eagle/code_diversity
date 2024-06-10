
def get_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

def get_max_lcm(arr):
    n = len(arr)
    max_lcm = 0
    for i in range(n-1):
        for j in range(i+1, n):
            lcm = get_lcm(arr[i], arr[j])
            if lcm > max_lcm:
                max_lcm = lcm
    return max_lcm

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_lcm(arr))

if __name__ == '__main__':
    main()

