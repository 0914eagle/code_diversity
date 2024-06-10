
def get_number_of_sodas(empty_bottles, found_bottles, cost_per_bottle):
    total_bottles = empty_bottles + found_bottles
    return total_bottles // cost_per_bottle

def main():
    empty_bottles, found_bottles, cost_per_bottle = map(int, input().split())
    print(get_number_of_sodas(empty_bottles, found_bottles, cost_per_bottle))

if __name__ == '__main__':
    main()

