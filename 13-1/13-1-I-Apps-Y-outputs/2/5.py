
s = input()
q = int(input())

for i in range(q):
    query = input().split()
    if query[0] == "1":
        s = s[:int(query[1])] + query[2] + s[int(query[1])+1:]
    else:
        print(len(set(s[int(query[1])-1:int(query[2])])))

