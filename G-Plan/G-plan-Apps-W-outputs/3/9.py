
def split_bacteria(total_mass):
    nights = 0
    split_pattern = []
    
    while total_mass > 1:
        max_mass_bacteria = total_mass // 2
        if max_mass_bacteria * 2 < total_mass:
            max_mass_bacteria += 1
        
        split_pattern.append(max_mass_bacteria)
        total_mass -= max_mass_bacteria
        nights += 1
    
    if total_mass == 1:
        return nights, split_pattern
    else:
        return -1, []

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        nights_needed, splitting_pattern = split_bacteria(n)
        
        print(nights_needed)
        if nights_needed != -1:
            print(*splitting_pattern)
