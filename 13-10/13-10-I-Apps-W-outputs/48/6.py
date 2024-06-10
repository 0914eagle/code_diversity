
def input_data():
    n = int(input())
    return n

def check_order(n):
    order = [0]
    visited = set()
    while len(order) < n:
        next_node = order[-1]
        if next_node == 0:
            next_node = 1
        else:
            next_node = (2 * next_node) % n
        if next_node in visited:
            return -1
        visited.add(next_node)
        order.append(next_node)
    return order

def main():
    n = input_data()
    order = check_order(n)
    if order == -1:
        print(-1)
    else:
        print(*order)

if __name__ == '__main__':
    main()

