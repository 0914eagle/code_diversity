
def solve_fuel_oil_problem(shipment_volume, bottle1_volume, bottle2_volume):
    if shipment_volume % bottle1_volume == 0:
        return shipment_volume // bottle1_volume, 0
    elif shipment_volume % bottle2_volume == 0:
        return 0, shipment_volume // bottle2_volume
    else:
        gcd = find_gcd(bottle1_volume, bottle2_volume)
        num1 = shipment_volume // (bottle1_volume // gcd)
        num2 = shipment_volume // (bottle2_volume // gcd)
        if num1 < num2:
            return num1, num2 - num1
        else:
            return num2, num1 - num2

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

