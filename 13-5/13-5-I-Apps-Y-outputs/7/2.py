
def get_input():
    return list(map(int, input().split()))

def get_seat_width():
    return get_input()[0]

def get_person_width():
    return get_input()[1]

def get_min_gap():
    return get_input()[2]

def can_fit_people(seat_width, person_width, min_gap):
    num_people = 0
    current_width = 0
    while current_width + person_width + min_gap <= seat_width:
        num_people += 1
        current_width += person_width + min_gap
    return num_people

def main():
    seat_width = get_seat_width()
    person_width = get_person_width()
    min_gap = get_min_gap()
    print(can_fit_people(seat_width, person_width, min_gap))

if __name__ == '__main__':
    main()

