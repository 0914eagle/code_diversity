
def f1(M):
    hours_until_new_year = 24 - M
    return hours_until_new_year

def f2():
    M = int(input())
    hours_until_new_year = f1(M)
    print(f"We have {hours_until_new_year} hours until New Year at {M}:00 on 30th, December.")

if __name__ == '__main__':
    f2()

