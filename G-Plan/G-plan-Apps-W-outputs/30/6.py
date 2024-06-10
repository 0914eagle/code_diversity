
def unlock_boxes(N, M, keys):
    boxes = [0] * (N + 1)
    for key in keys:
        price, num_boxes = key[0], key[1]
        for i in range(2, num_boxes + 2):
            boxes[key[i]] = price

    total_cost = 0
    for i in range(1, N + 1):
        if boxes[i] == 0:
            print(-1)
            return
        total_cost += boxes[i]

    print(total_cost)


if __name__ == "__main__":
    N, M = map(int, input().split())
    keys = [list(map(int, input().split())) for _ in range(M)]
    unlock_boxes(N, M, keys)
