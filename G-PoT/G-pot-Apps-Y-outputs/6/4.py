
b, d, c, l = map(int, input().split())

possible_answers = []
for i in range(b + 1):
    for j in range(d + 1):
        k = l - i*2 - j*4
        if k >= 0 and k <= c and i*2 + j*4 + k*4 == l:
            possible_answers.append((i, j, k))

if possible_answers:
    for answer in sorted(possible_answers):
        print(*answer)
else:
    print("impossible")
