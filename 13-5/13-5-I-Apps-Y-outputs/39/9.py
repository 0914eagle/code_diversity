
def get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume):
    large_bottles = shipment_volume // large_bottle_volume
    small_bottles = (shipment_volume - large_bottles * large_bottle_volume) // small_bottle_volume
    return large_bottles, small_bottles

def main():
    shipment_volume, large_bottle_volume, small_bottle_volume = map(int, input().split())
    large_bottles, small_bottles = get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume)
    print(large_bottles, small_bottles)

if __name__ == '__main__':
    main()

