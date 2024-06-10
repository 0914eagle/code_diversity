
import math

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def get_optimal_launch_window(year):
    if is_leap_year(year):
        return year % 26 == 1
    return year % 26 == 0

def main():
    year = int(input())
    if get_optimal_launch_window(year):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()

