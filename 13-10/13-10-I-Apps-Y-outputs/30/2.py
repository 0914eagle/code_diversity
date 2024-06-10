
def get_hours_until_new_year(h):
    return 24 - h

def main():
    h = int(input())
    hours_until_new_year = get_hours_until_new_year(h)
    print(f"We have {hours_until_new_year} hours until New Year at {h}:00 on 30th, December.")

if __name__ == '__main__':
    main()

