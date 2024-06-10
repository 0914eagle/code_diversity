
def get_number_of_sodas(empty_bottles, found_bottles, cost):
    num_sodas = 0
    while empty_bottles < cost:
        num_sodas += 1
        empty_bottles += 1
        if empty_bottles >= cost:
            break
    return num_sodas

def get_number_of_sodas_on_extra_thirsty_day(empty_bottles, found_bottles, cost):
    num_sodas = 0
    while empty_bottles < cost:
        num_sodas += 1
        empty_bottles += 1
        if empty_bottles >= cost:
            break
    empty_bottles += found_bottles
    return num_sodas

if __name__ == '__main__':
    empty_bottles, found_bottles, cost = map(int, input().split())
    print(get_number_of_sodas_on_extra_thirsty_day(empty_bottles, found_bottles, cost))

