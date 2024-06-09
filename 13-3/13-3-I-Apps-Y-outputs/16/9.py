
def is_heisei(date_string):
    date = datetime.strptime(date_string, "%Y/%m/%d")
    if date <= datetime(2019, 4, 30):
        return "Heisei"
    else:
        return "TBD"

def main():
    date_string = input()
    print(is_heisei(date_string))

if __name__ == '__main__':
    main()

