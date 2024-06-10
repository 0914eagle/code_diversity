
def count_binary_relations(n):
    def powerset(s):
        return map(set, chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    
    def is_reflexive(relation):
        return all(a in relation and b in relation[a] for a in relation for b in relation[a])
    
    def is_symmetric(relation):
        return all(b in relation and a in relation[b] for a in relation for b in relation[a])
    
    def is_transitive(relation):
        return all(c in relation[b] and b in relation[a] and a in relation for a in relation for b in relation[a] for c in relation[b])
    
    def count_non_reflexive_relations(n):
        non_reflexive_relations = 0
        for relation in powerset(range(n)):
            if is_symmetric(relation) and is_transitive(relation) and not is_reflexive(relation):
                non_reflexive_relations += 1
        return non_reflexive_relations
    
    return count_non_reflexive_relations(n) % (10**9 + 7)
    
if __name__ == '__main__':
    n = int(input())
    print(count_binary_relations(n))

