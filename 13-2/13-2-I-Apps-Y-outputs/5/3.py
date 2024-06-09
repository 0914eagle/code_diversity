
n = int(input())
words = input().split()

count = 0
for word in words:
    if word.isdigit():
        count += 1
    elif word == "mumble":
        count = 0

if count == n:
    print("makes sense")
else:
    print("something is fishy")

