
def get_input():
    return list(map(int, input().split()))

def get_max_people(seat_width, person_width, min_gap):
    return (seat_width - person_width) // (person_width + min_gap)

def main():
    seat_width, person_width, min_gap = get_input()
    print(get_max_people(seat_width, person_width, min_gap))

if __name__ == '__main__':
    main()

