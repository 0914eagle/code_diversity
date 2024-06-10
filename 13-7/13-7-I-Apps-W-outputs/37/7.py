
def get_pleasantness_sum(gift_ids, gift_pleasantnesses, chloe_gift_id, vladik_gift_id):
    chloe_gift_pleasantness = gift_pleasantnesses[chloe_gift_id - 1]
    vladik_gift_pleasantness = gift_pleasantnesses[vladik_gift_id - 1]
    chloe_gift_neighbors = get_gift_neighbors(gift_ids, chloe_gift_id)
    vladik_gift_neighbors = get_gift_neighbors(gift_ids, vladik_gift_id)
    intersection = set(chloe_gift_neighbors).intersection(vladik_gift_neighbors)
    if len(intersection) > 0:
        return "Impossible"
    else:
        return chloe_gift_pleasantness + vladik_gift_pleasantness + sum(gift_pleasantnesses[i - 1] for i in chloe_gift_neighbors) + sum(gift_pleasantnesses[i - 1] for i in vladik_gift_neighbors)

def get_gift_neighbors(gift_ids, gift_id):
    neighbors = []
    for i in range(len(gift_ids)):
        if gift_ids[i][0] == gift_id:
            neighbors.append(gift_ids[i][1])
        elif gift_ids[i][1] == gift_id:
            neighbors.append(gift_ids[i][0])
    return neighbors

def main():
    n = int(input())
    gift_ids = []
    gift_pleasantnesses = []
    for i in range(n):
        gift_ids.append(list(map(int, input().split())))
        gift_pleasantnesses.append(int(input()))
    chloe_gift_id = int(input())
    vladik_gift_id = int(input())
    print(get_pleasantness_sum(gift_ids, gift_pleasantnesses, chloe_gift_id, vladik_gift_id))

if __name__ == '__main__':
    main()

