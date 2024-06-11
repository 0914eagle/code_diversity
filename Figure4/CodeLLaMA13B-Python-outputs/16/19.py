def count_distinct_characters(string: str) -> int:
    
    return len({c.lower() for c in string})


if