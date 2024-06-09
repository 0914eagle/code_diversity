
def f1(k, d, t):
    # Calculate the time it takes to cook the chicken when the stove is turned on
    on_time = t

    # Calculate the time it takes to cook the chicken when the stove is turned off
    off_time = 2 * t

    # Calculate the total time it takes to cook the chicken
    total_time = on_time + off_time

    # Calculate the number of times Julia needs to turn on the stove
    num_turn_on = total_time // d

    # Calculate the number of minutes Julia needs to turn on the stove
    minutes_turn_on = num_turn_on * d

    # Calculate the number of minutes Julia needs to turn off the stove
    minutes_turn_off = total_time - minutes_turn_on

    # Calculate the total time it takes for Julia to cook the chicken
    total_cook_time = minutes_turn_on * on_time + minutes_turn_off * off_time

    return total_cook_time

def f2(k, d, t):
    # Calculate the time it takes for the stove to turn off after it is turned on
    off_time = k

    # Calculate the time it takes for Julia to turn on the stove
    turn_on_time = d

    # Calculate the total time it takes for Julia to cook the chicken
    total_cook_time = t * (off_time + turn_on_time)

    return total_cook_time

if __name__ == '__main__':
    k, d, t = map(int, input().split())
    print(f1(k, d, t))
    print(f2(k, d, t))

