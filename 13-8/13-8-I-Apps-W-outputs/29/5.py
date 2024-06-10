
def get_maximum_number_of_birds(wire_length, distance, number_of_birds):
    # Calculate the available length for the birds to sit
    available_length = wire_length - (number_of_birds * distance) - (2 * 6)
    # Calculate the maximum number of birds that can fit in the available length
    maximum_number_of_birds = available_length // distance
    return maximum_number_of_birds

def main():
    wire_length, distance, number_of_birds = map(int, input().split())
    print(get_maximum_number_of_birds(wire_length, distance, number_of_birds))

if __name__ == '__main__':
    main()

