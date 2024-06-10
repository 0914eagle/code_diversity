
def get_chest_numbers(n):
    chest_numbers = []
    for i in range(1, n+1):
        chest_numbers.append(i)
    return chest_numbers

def get_key_numbers(m):
    key_numbers = []
    for i in range(1, m+1):
        key_numbers.append(i)
    return key_numbers

def get_chest_key_pairs(chest_numbers, key_numbers):
    chest_key_pairs = []
    for chest_number in chest_numbers:
        for key_number in key_numbers:
            if (chest_number + key_number) % 2 == 1:
                chest_key_pairs.append((chest_number, key_number))
    return chest_key_pairs

def get_unique_chest_key_pairs(chest_key_pairs):
    unique_chest_key_pairs = []
    for pair in chest_key_pairs:
        if pair not in unique_chest_key_pairs:
            unique_chest_key_pairs.append(pair)
    return unique_chest_key_pairs

def get_opened_chests(unique_chest_key_pairs):
    opened_chests = set()
    for pair in unique_chest_key_pairs:
        opened_chests.add(pair[0])
    return opened_chests

def get_max_opened_chests(n, m):
    chest_numbers = get_chest_numbers(n)
    key_numbers = get_key_numbers(m)
    chest_key_pairs = get_chest_key_pairs(chest_numbers, key_numbers)
    unique_chest_key_pairs = get_unique_chest_key_pairs(chest_key_pairs)
    opened_chests = get_opened_chests(unique_chest_key_pairs)
    return len(opened_chests)

def main():
    n, m = map(int, input().split())
    chest_numbers = get_chest_numbers(n)
    key_numbers = get_key_numbers(m)
    print(get_max_opened_chests(n, m))

if __name__ == '__main__':
    main()

