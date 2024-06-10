
def split_bacteria(total_mass):
    nights = 0
    splitting_pattern = []
    
    while total_mass > 1:
        max_mass_bacteria = total_mass // 2
        splitting_pattern.append(max_mass_bacteria)
        total_mass -= max_mass_bacteria
        total_mass *= 2
        nights += 1
    
    if total_mass == 1:
        return nights, splitting_pattern
    else:
        return -1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        nights_needed, splitting_pattern = split_bacteria(n)
        
        if nights_needed == -1:
            print(-1)
        else:
            print(nights_needed)
            print(" ".join(map(str, splitting_pattern)))
