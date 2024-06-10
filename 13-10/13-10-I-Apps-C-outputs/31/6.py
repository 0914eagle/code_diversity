
def get_max_power(m, s, spell):
    # Initialize variables
    power = 1
    no_ops = 0
    max_power = 0
    max_no_ops = 0
    
    # Iterate through the spell
    for step in spell:
        if step == '+':
            power += 1
        else:
            power *= 2
        
        # Calculate the remaining power after discharging
        remaining_power = power % (2 ** s)
        
        # Check if the current power is greater than the maximum power
        if remaining_power > max_power:
            max_power = remaining_power
            max_no_ops = no_ops
        
        # Increment the number of no-ops
        no_ops += 1
    
    # Return the maximum power and the number of no-ops
    return max_power, max_no_ops

def get_optimal_spell(m, s, spell):
    # Get the maximum power and the number of no-ops
    max_power, max_no_ops = get_max_power(m, s, spell)
    
    # Initialize the optimal spell
    optimal_spell = ''
    
    # Iterate through the spell
    for i, step in enumerate(spell):
        if i < max_no_ops:
            optimal_spell += 'o'
        else:
            optimal_spell += step
    
    # Return the optimal spell
    return optimal_spell

if __name__ == '__main__':
    m, s = map(int, input().split())
    spell = input()
    optimal_spell = get_optimal_spell(m, s, spell)
    print(optimal_spell)

