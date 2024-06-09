
articles, impact_factor = map(int, input().split())
total_citations_needed = articles * impact_factor
bribes_needed = max(0, total_citations_needed - articles)
print(bribes_needed)
