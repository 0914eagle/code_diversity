
n = int(input())
a = list(map(int, input().split()))

x_count = 0
for x in set(a):
    positions = [i for i, a_i in enumerate(a) if a_i == x]
    if len(positions) > 1:
        common_diff = positions[1] - positions[0]
        for i in range(2, len(positions)):
            if positions[i] - positions[i-1] != common_diff:
                break
        else:
            x_count += 1
            print(x, common_diff)

print(x_count)

