
b, d, c, l = map(int, input().split())

possible_answers = []
for i in range(b + 1):
    for j in range(d + 1):
        k = l - i*2 - j*4
        if k >= 0 and k <= c*4:
            if k % 4 == 0:
                possible_answers.append((i, j, k//4))

if possible_answers:
    possible_answers.sort()
    for ans in possible_answers:
        print(*ans)
else:
    print("impossible")
