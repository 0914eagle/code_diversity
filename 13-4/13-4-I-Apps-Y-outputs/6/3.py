
def get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume):
    # Calculate the number of large bottles needed
    num_large_bottles = shipment_volume // large_bottle_volume
    
    # Calculate the number of small bottles needed
    num_small_bottles = (shipment_volume - (num_large_bottles * large_bottle_volume)) // small_bottle_volume
    
    # Check if the number of small bottles is greater than the number of large bottles
    if num_small_bottles > num_large_bottles:
        return "Impossible"
    
    # Return the number of large and small bottles needed
    return num_large_bottles, num_small_bottles

def main():
    shipment_volume, large_bottle_volume, small_bottle_volume = map(int, input().split())
    result = get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume)
    if result == "Impossible":
        print("Impossible")
    else:
        print(result[0], result[1])

if __name__ == '__main__':
    main()

