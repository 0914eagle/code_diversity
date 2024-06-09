
n = int(input())
proofs = []
for _ in range(n):
    p = int(input())
    proof_lengths = []
    for _ in range(p):
        l, k, *dependencies = map(int, input().split())
        proof_lengths.append((l, dependencies))
    proofs.append(proof_lengths)

dp = [0] * (1 << n)
for mask in range(1, 1 << n):
    dp[mask] = float('inf')
    for i in range(n):
        if mask & (1 << i):
            prev_mask = mask ^ (1 << i)
            current_length = 0
            for length, dependencies in proofs[i]:
                if all(prev_mask & (1 << d) for d in dependencies):
                    current_length = max(current_length, length)
            dp[mask] = min(dp[mask], dp[prev_mask] + current_length)

print(dp[(1 << n) - 1])
