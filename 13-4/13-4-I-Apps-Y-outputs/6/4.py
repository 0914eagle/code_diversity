
def get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume):
    # Calculate the number of large bottles needed
    large_bottles_needed = shipment_volume // large_bottle_volume
    
    # Calculate the number of small bottles needed
    small_bottles_needed = (shipment_volume - (large_bottles_needed * large_bottle_volume)) // small_bottle_volume
    
    # Check if the number of small bottles is greater than the number of large bottles
    if small_bottles_needed > large_bottles_needed:
        return "Impossible"
    
    # Return the number of large and small bottles needed
    return large_bottles_needed, small_bottles_needed

def main():
    shipment_volume, large_bottle_volume, small_bottle_volume = map(int, input().split())
    print(*get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume))

if __name__ == '__main__':
    main()

