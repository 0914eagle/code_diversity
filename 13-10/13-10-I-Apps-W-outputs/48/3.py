
def disarm(n):
    if n < 2 or n > 10**5:
        return -1
    order = [0]
    visited = set()
    while len(order) < n:
        curr = order[-1]
        next1 = (2*curr) % n
        next2 = (2*curr + 1) % n
        if next1 not in visited:
            order.append(next1)
            visited.add(next1)
        elif next2 not in visited:
            order.append(next2)
            visited.add(next2)
        else:
            return -1
    if order[0] != 0:
        return -1
    return order

def main():
    n = int(input())
    print(disarm(n))

if __name__ == '__main__':
    main()

