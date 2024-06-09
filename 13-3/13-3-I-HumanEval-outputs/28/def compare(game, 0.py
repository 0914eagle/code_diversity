
from typing import List

def compare(game: List[int], guess: List[int]) -> List[int]:
    
    result = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
    return result

