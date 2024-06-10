
def get_order(n):
    if n < 2 or n > 100000:
        return -1
    
    order = [0]
    visited = set()
    
    while len(order) < n:
        curr = order[-1]
        next_node = (2 * curr) % n
        if next_node not in visited:
            order.append(next_node)
            visited.add(next_node)
        else:
            next_node = (2 * curr) + 1 % n
            if next_node not in visited:
                order.append(next_node)
                visited.add(next_node)
            else:
                return -1
    
    return order

def main():
    n = int(input())
    order = get_order(n)
    if order == -1:
        print(-1)
    else:
        print(*order)

if __name__ == '__main__':
    main()

