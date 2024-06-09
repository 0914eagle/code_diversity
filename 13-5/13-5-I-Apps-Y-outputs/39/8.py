
def get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume):
    # Calculate the number of large bottles needed
    large_bottles_needed = shipment_volume // large_bottle_volume
    
    # Calculate the number of small bottles needed
    small_bottles_needed = (shipment_volume - (large_bottles_needed * large_bottle_volume)) // small_bottle_volume
    
    # Check if the number of small bottles is enough to fill the remaining space
    if small_bottles_needed * small_bottle_volume + (large_bottles_needed * large_bottle_volume) == shipment_volume:
        return large_bottles_needed, small_bottles_needed
    
    # If the number of small bottles is not enough, return "Impossible"
    else:
        return "Impossible"

def main():
    shipment_volume, large_bottle_volume, small_bottle_volume = map(int, input().split())
    print(get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume))

if __name__ == "__main__":
    main()

