
def is_valid_sequence(days):
    if len(days) > 24:
        return False
    
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 0
    for i in range(len(days)):
        month = days[i]
        if month > months[i % 12]:
            return False
        if month == 28 and i % 12 == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            continue
        if month == months[i % 12]:
            year += 1
    return True

def main():
    n = int(input())
    days = list(map(int, input().split()))
    print("YES") if is_valid_sequence(days) else print("NO")

if __name__ == '__main__':
    main()

