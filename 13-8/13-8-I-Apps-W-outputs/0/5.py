
def get_charge_difference(stone_charges, target_charges):
    
    return [target_charges[i] - stone_charges[i] for i in range(len(stone_charges))]

def synchronize(stone_charges, i):
    
    left_charge = stone_charges[i - 1]
    right_charge = stone_charges[i + 1]
    stone_charges[i] = left_charge + right_charge - stone_charges[i]

def can_synchronize(stone_charges, target_charges):
    
    difference = get_charge_difference(stone_charges, target_charges)
    if all(difference == 0):
        return True
    for i in range(1, len(stone_charges) - 1):
        if difference[i] != 0:
            continue
        synchronize(stone_charges, i)
        difference = get_charge_difference(stone_charges, target_charges)
        if all(difference == 0):
            return True
    return False

def main():
    n = int(input())
    stone_charges = list(map(int, input().split()))
    target_charges = list(map(int, input().split()))
    if can_synchronize(stone_charges, target_charges):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

