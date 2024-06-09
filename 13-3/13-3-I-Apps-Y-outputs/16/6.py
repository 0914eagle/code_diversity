
def is_heisei(date_string):
    date = datetime.strptime(date_string, "%Y/%m/%d")
    if date <= datetime(2019, 4, 30):
        return "Heisei"
    else:
        return "TBD"

if __name__ == "__main__":
    date_string = input()
    print(is_heisei(date_string))

