
def get_input():
    return list(map(int, input().split()))

def seat_people(seat_width, person_width, gap):
    return (seat_width - person_width) // (person_width + gap)

def main():
    seat_width, person_width, gap = get_input()
    print(seat_people(seat_width, person_width, gap))

if __name__ == '__main__':
    main()

