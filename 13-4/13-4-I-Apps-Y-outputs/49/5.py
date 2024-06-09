
x, y = input().split()

if x == 'A':
    x_value = 10
elif x == 'B':
    x_value = 11
elif x == 'C':
    x_value = 12
elif x == 'D':
    x_value = 13
elif x == 'E':
    x_value = 14
else:
    x_value = 15

if y == 'A':
    y_value = 10
elif y == 'B':
    y_value = 11
elif y == 'C':
    y_value = 12
elif y == 'D':
    y_value = 13
elif y == 'E':
    y_value = 14
else:
    y_value = 15

if x_value < y_value:
    print('<')
elif x_value > y_value:
    print('>')
else:
    print('=')

