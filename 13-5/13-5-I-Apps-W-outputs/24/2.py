
def get_initial_order(current_order):
    n = len(current_order)
    initial_order = [0] * n
    for i in range(n):
        initial_order[i] = current_order[i]
    for i in range(n):
        for j in range(i, n):
            if initial_order[i] > initial_order[j]:
                temp = initial_order[i]
                initial_order[i] = initial_order[j]
                initial_order[j] = temp
    return initial_order

def main():
    n = int(input())
    current_order = list(map(int, input().split()))
    initial_order = get_initial_order(current_order)
    print(*initial_order)

if __name__ == '__main__':
    main()

