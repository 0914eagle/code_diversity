
def get_pleasantness_sum(chloe_gift, vladik_gift, gifts, edges):
    chloe_gifts = [chloe_gift]
    vladik_gifts = [vladik_gift]
    while chloe_gifts or vladik_gifts:
        if chloe_gifts:
            current_gift = chloe_gifts.pop()
            for edge in edges:
                if edge[0] == current_gift:
                    chloe_gifts.append(edge[1])
        if vladik_gifts:
            current_gift = vladik_gifts.pop()
            for edge in edges:
                if edge[0] == current_gift:
                    vladik_gifts.append(edge[1])
    return sum(gifts[gift] for gift in set(chloe_gifts + vladik_gifts))

def solve(n, a, edges):
    gifts = {i: a[i-1] for i in range(1, n+1)}
    edges = [(i[0], i[1]) for i in edges]
    max_sum = -float('inf')
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                sum_i_j = get_pleasantness_sum(i, j, gifts, edges)
                if sum_i_j > max_sum:
                    max_sum = sum_i_j
    if max_sum == -float('inf'):
        return 'Impossible'
    else:
        return max_sum

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    print(solve(n, a, edges))

