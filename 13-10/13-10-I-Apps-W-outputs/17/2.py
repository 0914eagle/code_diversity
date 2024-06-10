
def find_min_distance(n, k, string):
    # Find the index of the first k + 1 free rooms
    free_rooms = [i for i, c in enumerate(string) if c == '0']
    first_free_room = free_rooms[k]

    # Find the index of the last free room
    last_free_room = free_rooms[-1]

    # Calculate the minimum distance between the first and last free room
    min_distance = abs(first_free_room - last_free_room)

    return min_distance

def main():
    n, k = map(int, input().split())
    string = input()
    print(find_min_distance(n, k, string))

if __name__ == '__main__':
    main()

