def valid_date(date):
    
    if len(date) == 0:
        return False
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    month, day, year = int(month), int(day), int(year)
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2 and day > 29:
        return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(valid_date('01-01-2000'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert valid_date('01-01-2000') == True
    assert valid_date('04-04-2020') == True
    assert valid_date('06-04-2020') == True
    assert valid_date('06-04-2021') == False
    assert valid_date('06-04-2021') == False
    assert valid_date('06-04-2021') == False
    assert valid_date('06-04-2021') == False
    assert valid_date('06-04-2021') == False
    assert valid_date('06-04-2021') == False
    assert valid_date('06-04-2021') == False
    assert valid_date('06-04-2021') == False
    assert valid_date('06-04-2