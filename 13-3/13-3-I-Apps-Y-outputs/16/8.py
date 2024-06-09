
def is_before_april_30_2019(date_string):
    date = datetime.strptime(date_string, "%Y/%m/%d")
    april_30_2019 = datetime(2019, 4, 30)
    return date <= april_30_2019

def solve(date_string):
    if is_before_april_30_2019(date_string):
        return "Heisei"
    else:
        return "TBD"

if __name__ == "__main__":
    date_string = input()
    print(solve(date_string))

