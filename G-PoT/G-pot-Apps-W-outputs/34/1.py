
word = input()

if 'CODEFORCES' in word:
    print('YES')
else:
    for i in range(len(word)):
        if 'CODEFORCES' in word[:i] + word[i+len('CODEFORCES'):]:
            print('YES')
            break
    else:
        print('NO')
