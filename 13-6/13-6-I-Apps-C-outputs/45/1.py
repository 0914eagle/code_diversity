
def get_total_time(k, d, t):
    # Calculate the time the chicken takes to cook on the stove when it is turned on
    on_time = t

    # Calculate the time the chicken takes to cook on the stove when it is turned off
    off_time = 2 * t

    # Calculate the total time Julia needs to turn the stove on and off
    total_on_off_time = (k - 1) / d

    # Calculate the total time Julia needs to turn the stove on and off, including the time the chicken takes to cook
    total_time = total_on_off_time * on_time + (total_on_off_time - 1) * off_time

    return total_time

def main():
    k, d, t = map(int, input().split())
    print(get_total_time(k, d, t))

if __name__ == '__main__':
    main()

