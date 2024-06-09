
A, B, and C are equal if A == B and B == C, so we can check if A == B and B == C using the and operator. If either of these conditions is not met, we can return "No".

If A == B and B == C, we can check if B is different from A using the != operator. If B is not different from A, we can return "No".

If B is different from A and A == B and B == C, we can return "Yes".

Here's the code:
```
A, B, C = map(int, input().split())
if A == B and B == C:
    if B != A:
        print("Yes")
    else:
        print("No")
else:
    print("No")
```

