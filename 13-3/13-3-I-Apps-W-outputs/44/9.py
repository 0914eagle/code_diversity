
n = int(input())

# Calculate the maximum height of the pyramid
max_height = 1
while n >= max_height:
    max_height += 1
    n -= max_height

print(max_height)

