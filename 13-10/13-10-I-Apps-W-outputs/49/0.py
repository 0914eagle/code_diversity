
def get_tshirt_sizes():
    return list(map(int, input().split()))

def get_number_of_participants():
    return int(input())

def get_participant_sizes():
    sizes = []
    for _ in range(get_number_of_participants()):
        sizes.append(input())
    return sizes

def is_valid_distribution(sizes, tshirt_sizes):
    for size in sizes:
        if size == "S":
            if tshirt_sizes[0] == 0:
                return False
            tshirt_sizes[0] -= 1
        elif size == "M":
            if tshirt_sizes[1] == 0:
                return False
            tshirt_sizes[1] -= 1
        elif size == "L":
            if tshirt_sizes[2] == 0:
                return False
            tshirt_sizes[2] -= 1
        elif size == "XL":
            if tshirt_sizes[3] == 0:
                return False
            tshirt_sizes[3] -= 1
        elif size == "XXL":
            if tshirt_sizes[4] == 0:
                return False
            tshirt_sizes[4] -= 1
        elif size == "XXXL":
            if tshirt_sizes[5] == 0:
                return False
            tshirt_sizes[5] -= 1
    return True

def find_valid_distribution(sizes, tshirt_sizes):
    if is_valid_distribution(sizes, tshirt_sizes):
        return sizes
    else:
        return None

def main():
    tshirt_sizes = get_tshirt_sizes()
    sizes = get_participant_sizes()
    result = find_valid_distribution(sizes, tshirt_sizes)
    if result is None:
        print("NO")
    else:
        print("YES")
        for size in result:
            print(size)

if __name__ == '__main__':
    main()

