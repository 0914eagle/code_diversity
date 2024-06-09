
def get_input():
    return list(map(int, input().split()))

def get_maximum_people(seat_width, person_width, minimum_gap):
    return (seat_width - person_width) // (person_width + minimum_gap)

def main():
    seat_width, person_width, minimum_gap = get_input()
    print(get_maximum_people(seat_width, person_width, minimum_gap))

if __name__ == '__main__':
    main()

