
def get_bottles(shipment_volume, bottle1_volume, bottle2_volume):
    # Initialize variables
    num_bottles1 = 0
    num_bottles2 = 0
    remaining_volume = shipment_volume

    # Calculate the number of bottles of size bottle1_volume that can be filled
    num_bottles1 = remaining_volume // bottle1_volume
    remaining_volume %= bottle1_volume

    # Calculate the number of bottles of size bottle2_volume that can be filled
    num_bottles2 = remaining_volume // bottle2_volume

    # Check if the conditions are met
    if num_bottles1 * bottle1_volume + num_bottles2 * bottle2_volume == shipment_volume:
        return num_bottles1, num_bottles2
    else:
        return "Impossible"

def main():
    shipment_volume, bottle1_volume, bottle2_volume = map(int, input().split())
    num_bottles1, num_bottles2 = get_bottles(shipment_volume, bottle1_volume, bottle2_volume)
    print(num_bottles1, num_bottles2)

if __name__ == '__main__':
    main()

