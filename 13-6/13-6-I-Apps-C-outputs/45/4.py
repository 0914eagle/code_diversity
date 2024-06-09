
def f1(k, d, t):
    # Calculate the time it takes to cook the chicken when the stove is on
    time_on = t
    
    # Calculate the time it takes to cook the chicken when the stove is off
    time_off = 2 * t
    
    # Calculate the total time it takes to cook the chicken
    total_time = time_on + time_off
    
    # Calculate the number of times Julia needs to turn on the stove
    num_turn_on = total_time // k
    
    # Calculate the time it takes for Julia to turn on the stove
    time_turn_on = num_turn_on * d
    
    # Calculate the total time it takes for Julia to cook the chicken
    total_time_cook = total_time + time_turn_on
    
    return total_time_cook

def f2(k, d, t):
    # Calculate the time it takes to cook the chicken when the stove is on
    time_on = t
    
    # Calculate the time it takes to cook the chicken when the stove is off
    time_off = 2 * t
    
    # Calculate the total time it takes to cook the chicken
    total_time = time_on + time_off
    
    # Calculate the number of times Julia needs to turn on the stove
    num_turn_on = total_time // k
    
    # Calculate the time it takes for Julia to turn on the stove
    time_turn_on = num_turn_on * d
    
    # Calculate the total time it takes for Julia to cook the chicken
    total_time_cook = total_time + time_turn_on
    
    return total_time_cook

if __name__ == '__main__':
    k, d, t = map(int, input().split())
    print(f1(k, d, t))
    print(f2(k, d, t))

