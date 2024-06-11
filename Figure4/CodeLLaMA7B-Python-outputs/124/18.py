def valid_date(date):
    
    if date == "":
        return False
    date_list = date.split("-")
    if len(date_list) != 3:
        return False
    if int(date_list[0]) < 1 or int(date_list[0]) > 12:
        return False
    if int(date_list[0]) in [1, 3, 5, 7, 8, 10, 12]:
        if int(date_list[1]) < 1 or int(date_list[1]) > 31:
            return False
    elif int(date_list[0]) in [4, 6, 9, 11]:
        if int(date_list[1]) < 1 or int(date_list[1]) > 30:
            return False
    elif int(date_list[0]) == 2:
        if int(date_list[1]) < 1 or int(date_list[1]) > 29:
            return False
    if int(date_list[2]) < 0 or int(date_list[2]) > 9999:
        return False
    return True


if __name__ == "__main__":
    print(valid_date("03-11-2000"))
    print(valid_date("15-01-2012"))
    print(valid_date("04-0-2040"))
    print(valid_date("06-04-2020"))
    print(valid_date("06/04/2020"))
