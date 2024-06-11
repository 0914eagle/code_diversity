
from typing import List


def all_prefixes(string: str) -> List[str]:
    
    return [string[0:i+1] for i in range(len(string))]

