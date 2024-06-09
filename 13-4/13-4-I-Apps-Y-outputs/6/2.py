
def get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume):
    if large_bottle_volume < small_bottle_volume:
        return "Impossible"
    
    large_bottles = shipment_volume // large_bottle_volume
    small_bottles = (shipment_volume - large_bottles * large_bottle_volume) // small_bottle_volume
    
    if large_bottles + small_bottles < shipment_volume:
        large_bottles += 1
    
    return large_bottles, small_bottles

def main():
    shipment_volume, large_bottle_volume, small_bottle_volume = map(int, input().split())
    print(*get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume))

if __name__ == '__main__':
    main()

