
def get_bottles(shipment_volume, bottle1_volume, bottle2_volume):
    # Initialize variables
    num_bottle1 = 0
    num_bottle2 = 0
    total_volume = 0

    # Loop until the shipment is filled or the conditions cannot be met
    while total_volume < shipment_volume and num_bottle1 * bottle1_volume + num_bottle2 * bottle2_volume > 0:
        # Check if the current combination of bottles fulfills the conditions
        if total_volume + bottle1_volume <= shipment_volume:
            total_volume += bottle1_volume
            num_bottle1 += 1
        elif total_volume + bottle2_volume <= shipment_volume:
            total_volume += bottle2_volume
            num_bottle2 += 1
        else:
            break

    # Check if the conditions cannot be met
    if total_volume < shipment_volume or num_bottle1 * bottle1_volume + num_bottle2 * bottle2_volume == 0:
        return "Impossible"

    # Return the number of bottles of each size
    return num_bottle1, num_bottle2

def main():
    shipment_volume, bottle1_volume, bottle2_volume = map(int, input().split())
    num_bottle1, num_bottle2 = get_bottles(shipment_volume, bottle1_volume, bottle2_volume)
    print(num_bottle1, num_bottle2)

if __name__ == '__main__':
    main()

