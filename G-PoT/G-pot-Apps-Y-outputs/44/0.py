
articles, impact_factor = map(int, input().split())
total_citations_needed = articles * impact_factor
bribed_scientists = max(0, total_citations_needed - articles)
print(bribed_scientists)
