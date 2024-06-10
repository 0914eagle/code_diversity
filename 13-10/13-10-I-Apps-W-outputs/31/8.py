
def is_possible(a, b, c):
    # Check if the sum of the valence numbers is even
    if a + b + c % 2 == 1:
        return False
    
    # Check if the valence numbers are in ascending order
    if a >= b or b >= c:
        return False
    
    # Check if the valence numbers are perfect squares
    if a**0.5 != int(a**0.5) or b**0.5 != int(b**0.5) or c**0.5 != int(c**0.5):
        return False
    
    return True

def get_bonds(a, b, c):
    # Find the number of bonds between each pair of atoms
    bond_12 = int((a + b) / 2)
    bond_23 = int((b + c) / 2)
    bond_31 = int((c + a) / 2)
    
    return bond_12, bond_23, bond_31

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    
    if is_possible(a, b, c):
        print(*get_bonds(a, b, c))
    else:
        print("Impossible")

