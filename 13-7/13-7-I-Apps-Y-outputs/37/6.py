
def is_optimal_launch_window(year):
    # Calculate the number of months since 2018
    months_since_2018 = 12 * (year - 2018)
    
    # Check if the number of months is divisible by 26
    if months_since_2018 % 26 == 0:
        return "yes"
    else:
        return "no"

def main():
    year = int(input())
    print(is_optimal_launch_window(year))

if __name__ == '__main__':
    main()

