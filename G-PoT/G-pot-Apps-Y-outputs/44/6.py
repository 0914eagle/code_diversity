
articles, impact_factor = map(int, input().split())

total_citations_needed = articles * impact_factor
total_citations_current = 0

scientists_bribed = 0

while total_citations_current < total_citations_needed:
    total_citations_current += articles
    scientists_bribed += 1

print(scientists_bribed)
