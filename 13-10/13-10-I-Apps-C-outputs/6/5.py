
def fight(attacker_ap, attacker_hp, enemy_ap, enemy_hp):
    
    while attacker_hp > 0 and enemy_hp > 0:
        attacker_hp -= enemy_ap
        enemy_hp -= attacker_ap
    if attacker_hp > enemy_hp:
        return "Unnar", attacker_hp
    else:
        return "Enemy", enemy_hp


def find_safe_path(unnar_ap, unnar_hp, areas, passages):
    
    visited = set()
    queue = [(1, unnar_ap, unnar_hp)]
    while queue:
        current_area, current_ap, current_hp = queue.pop(0)
        if current_area == len(areas):
            return current_hp
        if current_area in visited:
            continue
        visited.add(current_area)
        for passage in passages:
            if passage[0] == current_area:
                enemy_ap, enemy_hp = passage[2], passage[3]
                winner, remaining_hp = fight(current_ap, current_hp, enemy_ap, enemy_hp)
                if winner == "Unnar":
                    queue.append((passage[1], current_ap, remaining_hp))
    return 0


def main():
    unnar_ap, unnar_hp = map(int, input().split())
    areas = int(input())
    passages = []
    for _ in range(areas - 1):
        passage = list(map(int, input().split()))
        passages.append(passage)
    safe_path = find_safe_path(unnar_ap, unnar_hp, areas, passages)
    if safe_path == 0:
        print("Oh no")
    else:
        print(safe_path)


if __name__ == '__main__':
    main()

