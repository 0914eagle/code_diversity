
def get_additional_birds(length, distance, num_birds, positions):
    # Calculate the available space for additional birds
    available_space = length - num_birds * distance - 6

    # Check if there is enough space for all the additional birds
    if available_space >= num_birds * distance:
        return num_birds

    # Calculate the maximum number of additional birds that can fit
    return int(available_space / distance)

def main():
    length, distance, num_birds = map(int, input().split())
    positions = [int(input()) for _ in range(num_birds)]
    print(get_additional_birds(length, distance, num_birds, positions))

if __name__ == '__main__':
    main()

