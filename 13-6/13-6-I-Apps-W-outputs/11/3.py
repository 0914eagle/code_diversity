
def get_target_weight(weights):
    total_weight = sum(weights)
    num_animals = len(weights)
    for t in range(1, total_weight + 1):
        if t * 2 == total_weight:
            return t
        if t * 2 < total_weight:
            if num_animals % 2 == 0:
                return t
            else:
                return t + 1
    return -1

def main():
    num_animals = int(input())
    weights = []
    for i in range(num_animals):
        weights.append(int(input()))
    print(get_target_weight(weights))

if __name__ == '__main__':
    main()

