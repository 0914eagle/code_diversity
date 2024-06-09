
def get_input():
    return list(map(int, input().split()))

def get_max_people(seat_width, person_width, gap_width):
    return (seat_width - person_width) // (person_width + gap_width)

def main():
    seat_width, person_width, gap_width = get_input()
    print(get_max_people(seat_width, person_width, gap_width))

if __name__ == '__main__':
    main()

