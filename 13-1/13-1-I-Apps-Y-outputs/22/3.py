
def f1(n, a):
    sheet = set()
    for i in range(n):
        if a[i] in sheet:
            sheet.remove(a[i])
        else:
            sheet.add(a[i])
    return len(sheet)

