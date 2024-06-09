
def get_bottle_counts(shipment_volume, bottle1_volume, bottle2_volume):
    # Initialize variables
    bottle1_count = 0
    bottle2_count = 0
    remaining_volume = shipment_volume

    # Calculate the number of bottles of size bottle1_volume that can be filled
    while remaining_volume >= bottle1_volume:
        bottle1_count += 1
        remaining_volume -= bottle1_volume

    # Calculate the number of bottles of size bottle2_volume that can be filled
    while remaining_volume >= bottle2_volume:
        bottle2_count += 1
        remaining_volume -= bottle2_volume

    # Check if the conditions are met
    if remaining_volume == 0 and bottle1_count > 0 and bottle2_count > 0:
        return bottle1_count, bottle2_count
    else:
        return "Impossible"

def main():
    shipment_volume, bottle1_volume, bottle2_volume = map(int, input().split())
    print(get_bottle_counts(shipment_volume, bottle1_volume, bottle2_volume))

if __name__ == "__main__":
    main()

