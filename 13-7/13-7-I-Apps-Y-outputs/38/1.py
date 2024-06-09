
def get_names(n):
    names = []
    for _ in range(n):
        first_name, last_name, age, sex = input().split()
        if sex == 'M':
            title = 'Mr.'
        else:
            title = 'Ms.'
        names.append([title, first_name, last_name, int(age)])
    return sorted(names, key=lambda x: (x[3], x[0], x[1]))

