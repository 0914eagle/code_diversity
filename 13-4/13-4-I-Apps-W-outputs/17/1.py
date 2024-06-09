
x = int(input())
result = ""
while x > 0:
    result = str(9 - x % 10) + result
    x //= 10
print(int(result))

