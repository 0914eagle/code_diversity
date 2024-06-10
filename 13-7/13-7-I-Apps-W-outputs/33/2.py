
def get_smallest_index_to_exit(doors):
    left_doors = 0
    right_doors = 0
    for i, door in enumerate(doors):
        if door == 0:
            left_doors += 1
        else:
            right_doors += 1
        if left_doors > 0 and right_doors > 0:
            return i
    return len(doors)

def main():
    n = int(input())
    doors = list(map(int, input().split()))
    print(get_smallest_index_to_exit(doors))

if __name__ == '__main__':
    main()

