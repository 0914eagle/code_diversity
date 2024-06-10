
def get_hours_until_new_year(time):
    return 24 - time

def main():
    time = int(input())
    hours = get_hours_until_new_year(time)
    print(f"We have {hours} hours until New Year at {time}:00 on 30th, December.")

if __name__ == '__main__':
    main()

