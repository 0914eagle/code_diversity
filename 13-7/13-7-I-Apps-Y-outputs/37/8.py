
def is_optimal_launch_window(year):
    # Calculate the number of months since 2018
    months_since_2018 = 12 * (year - 2018)
    
    # Calculate the number of months since the last optimal launch window
    months_since_last_window = months_since_2018 % 26
    
    # Check if there is an optimal launch window in the current year
    if months_since_last_window == 0:
        return "yes"
    else:
        return "no"

def main():
    year = int(input())
    print(is_optimal_launch_window(year))

if __name__ == '__main__':
    main()

