
def get_num_sodas(empty_bottles, found_bottles, cost_per_bottle):
    num_sodas = 0
    while empty_bottles < cost_per_bottle:
        num_sodas += 1
        empty_bottles += found_bottles
    return num_sodas

def get_total_sodas(empty_bottles, found_bottles, cost_per_bottle):
    num_sodas = get_num_sodas(empty_bottles, found_bottles, cost_per_bottle)
    total_sodas = num_sodas + empty_bottles // cost_per_bottle
    return total_sodas

if __name__ == '__main__':
    e, f, c = map(int, input().split())
    print(get_total_sodas(e, f, c))

