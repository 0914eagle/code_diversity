
def get_sodas_drunk(empty_bottles, found_bottles, cost):
    total_bottles = empty_bottles + found_bottles
    sodas_drunk = total_bottles // cost
    return sodas_drunk

def get_empty_bottles(sodas_drunk, cost):
    empty_bottles = sodas_drunk * cost
    return empty_bottles

if __name__ == '__main__':
    empty_bottles, found_bottles, cost = map(int, input().split())
    sodas_drunk = get_sodas_drunk(empty_bottles, found_bottles, cost)
    empty_bottles = get_empty_bottles(sodas_drunk, cost)
    print(sodas_drunk)

