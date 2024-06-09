
def f1(N, A):
    sheet = set()
    for i in range(N):
        if A[i] in sheet:
            sheet.remove(A[i])
        else:
            sheet.add(A[i])
    return len(sheet)

