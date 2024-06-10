
def max_power(M, S, steps):
    # Initialize variables
    power = 1
    no_ops = 0
    max_power = 0
    optimal_steps = []

    # Iterate through the steps
    for i, step in enumerate(steps):
        # If the step is a + step, add 1 to the power
        if step == "+":
            power += 1
        # If the step is an x step, multiply the power by 2
        elif step == "x":
            power *= 2
        # If the step is a no-op step, do nothing
        else:
            no_ops += 1

        # Calculate the maximum power that can be discharged
        max_power = power // (2 ** S)

        # If the maximum power is greater than the current optimal power, update the optimal power and the list of optimal steps
        if max_power > optimal_power:
            optimal_power = max_power
            optimal_steps = steps[:i] + ["o"] + steps[i+1:]

    # Return the list of optimal steps
    return optimal_steps

def main():
    M, S = map(int, input().split())
    steps = list(input())
    optimal_steps = max_power(M, S, steps)
    print("".join(optimal_steps))

if __name__ == "__main__":
    main()

