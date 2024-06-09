
def get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume):
    # Calculate the number of large bottles needed
    large_bottles_needed = shipment_volume // large_bottle_volume
    
    # Calculate the number of small bottles needed
    small_bottles_needed = (shipment_volume - (large_bottles_needed * large_bottle_volume)) // small_bottle_volume
    
    # Check if the number of small bottles is divisible by the number of large bottles
    if small_bottles_needed % large_bottles_needed == 0:
        return large_bottles_needed, small_bottles_needed
    else:
        return "Impossible"

def main():
    shipment_volume, large_bottle_volume, small_bottle_volume = map(int, input().split())
    print(*get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume))

if __name__ == '__main__':
    main()

