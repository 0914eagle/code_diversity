
def get_min_max_occupied_houses(x):
    n = len(x)
    min_occupied_houses = 0
    max_occupied_houses = 0
    for i in range(n):
        min_occupied_houses += 1
        max_occupied_houses += 2
        if x[i] == 1 or x[i] == n:
            min_occupied_houses -= 1
            max_occupied_houses -= 1
        if x[i] == 1 and x[i+1] == 2:
            min_occupied_houses -= 1
        if x[i] == n and x[i-1] == n-1:
            min_occupied_houses -= 1
    return min_occupied_houses, max_occupied_houses

def main():
    n = int(input())
    x = list(map(int, input().split()))
    min_occupied_houses, max_occupied_houses = get_min_max_occupied_houses(x)
    print(min_occupied_houses, max_occupied_houses)

if __name__ == '__main__':
    main()

