def valid_date(date):
    
    import datetime
    import re

    if date == "":
        return False

    if not re.match(r"^[0-9]{2}\-[0-9]{2}\-[0-9]{4}$", date):
        return False

    month, day, year = date.split("-")

    try:
        datetime.date(int(year), int(month), int(day))
    except ValueError:
        return False

    return True


if __name__ == "__main__":
    print(valid_date("03-11-2000"))
    print(valid_date("15-01-2012"))
    print(valid_date("04-0-2040"))
    print(valid_date("06-04-2020"))
    print(valid_date("06/04/2020"))
