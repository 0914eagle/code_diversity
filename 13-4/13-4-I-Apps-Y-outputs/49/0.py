
x, y = input().split()

if x == 'A':
    x_val = 10
elif x == 'B':
    x_val = 11
elif x == 'C':
    x_val = 12
elif x == 'D':
    x_val = 13
elif x == 'E':
    x_val = 14
elif x == 'F':
    x_val = 15

if y == 'A':
    y_val = 10
elif y == 'B':
    y_val = 11
elif y == 'C':
    y_val = 12
elif y == 'D':
    y_val = 13
elif y == 'E':
    y_val = 14
elif y == 'F':
    y_val = 15

if x_val < y_val:
    print('<')
elif x_val > y_val:
    print('>')
else:
    print('=')

