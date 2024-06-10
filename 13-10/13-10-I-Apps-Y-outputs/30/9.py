
def get_hours_until_new_year(m):
    current_hour = int(m)
    total_hours = 24 - current_hour
    return total_hours

def main():
    m = input("Enter the current hour: ")
    hours_until_new_year = get_hours_until_new_year(m)
    print(f"We have {hours_until_new_year} hours until New Year at {m} o'clock on 30th, December.")

if __name__ == '__main__':
    main()

