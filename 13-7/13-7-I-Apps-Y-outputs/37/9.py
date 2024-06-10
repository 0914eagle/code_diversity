
def is_optimal_launch_window(year):
    # Check if the year is between 2018 and 10000
    if not (2018 <= year <= 10000):
        return "Invalid input"
    
    # Check if the year is a multiple of 26
    if year % 26 == 0:
        return "yes"
    else:
        return "no"

def main():
    year = int(input("Enter a year: "))
    print(is_optimal_launch_window(year))

if __name__ == '__main__':
    main()

