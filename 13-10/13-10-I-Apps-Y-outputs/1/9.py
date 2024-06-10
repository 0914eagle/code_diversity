
def get_num_sodas(empty_bottles, empty_bottles_found, cost_per_soda):
    num_sodas = 0
    while empty_bottles < cost_per_soda:
        num_sodas += 1
        empty_bottles += empty_bottles_found
    return num_sodas

def main():
    empty_bottles, empty_bottles_found, cost_per_soda = map(int, input().split())
    print(get_num_sodas(empty_bottles, empty_bottles_found, cost_per_soda))

if __name__ == '__main__':
    main()

