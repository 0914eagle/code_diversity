
def move_girls_in_front_of_boys(line):
    boys = 0
    girls = 0
    swaps = 0

    for char in line:
        if char == 'M':
            boys += 1
        else:
            girls += 1
            swaps += boys

    return swaps

if __name__ == '__main__':
    line = input().strip()
    print(move_girls_in_front_of_boys(line))
