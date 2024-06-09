
def get_bottles(shipment_volume, bottle1_volume, bottle2_volume):
    # Initialize variables
    num_bottles1 = 0
    num_bottles2 = 0
    total_volume = 0

    # Calculate the number of bottles of size bottle1_volume needed
    num_bottles1 = shipment_volume // bottle1_volume
    total_volume += num_bottles1 * bottle1_volume

    # Calculate the number of bottles of size bottle2_volume needed
    num_bottles2 = (shipment_volume - total_volume) // bottle2_volume
    total_volume += num_bottles2 * bottle2_volume

    # Check if the total volume is equal to the shipment volume
    if total_volume == shipment_volume:
        return num_bottles1, num_bottles2
    else:
        return "Impossible"

def main():
    shipment_volume, bottle1_volume, bottle2_volume = map(int, input().split())
    num_bottles1, num_bottles2 = get_bottles(shipment_volume, bottle1_volume, bottle2_volume)
    print(num_bottles1, num_bottles2)

if __name__ == '__main__':
    main()

