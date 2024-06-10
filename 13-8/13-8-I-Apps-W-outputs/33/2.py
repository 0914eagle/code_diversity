
def get_group_cost(group_size, c1, c2):
    if group_size == 1:
        return c1
    else:
        return c1 + c2 * (group_size - 1) ** 2

def get_min_cost(n, c1, c2, visitors):
    groups = []
    current_group = []
    for i in range(n):
        if visitors[i] == 0:
            current_group.append(i)
        else:
            groups.append(current_group)
            current_group = []
    
    groups.append(current_group)
    
    total_cost = 0
    for group in groups:
        total_cost += get_group_cost(len(group), c1, c2)
    
    return total_cost

def main():
    n, c1, c2 = map(int, input().split())
    visitors = list(map(int, input()))
    print(get_min_cost(n, c1, c2, visitors))

if __name__ == '__main__':
    main()

