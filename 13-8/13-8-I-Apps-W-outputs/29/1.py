
def get_bird_positions(n):
    positions = []
    for i in range(n):
        positions.append(int(input()))
    return positions

def get_max_additional_birds(l, d, n, positions):
    positions.sort()
    max_additional_birds = 0
    for i in range(n):
        if positions[i] + d + 6 > l:
            break
        max_additional_birds += 1
    return max_additional_birds

def main():
    l, d, n = map(int, input().split())
    positions = get_bird_positions(n)
    print(get_max_additional_birds(l, d, n, positions))

if __name__ == '__main__':
    main()

