
def get_pleasantness_sum(gifts, chosen_gifts):
    pleasantness_sum = 0
    for gift in chosen_gifts:
        pleasantness_sum += gifts[gift - 1]
    return pleasantness_sum

def choose_prizes(gifts, edges):
    n = len(gifts)
    chosen_gifts = set()
    for i in range(n):
        if i not in chosen_gifts:
            for j in range(i + 1, n):
                if j not in chosen_gifts and (i, j) in edges or (j, i) in edges:
                    chosen_gifts.add(i)
                    chosen_gifts.add(j)
                    break
    
    if len(chosen_gifts) == n:
        return get_pleasantness_sum(gifts, chosen_gifts)
    else:
        return -1

def main():
    n = int(input())
    gifts = list(map(int, input().split()))
    edges = set()
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.add((u, v))
    
    result = choose_prizes(gifts, edges)
    if result == -1:
        print("Impossible")
    else:
        print(result)

if __name__ == '__main__':
    main()

