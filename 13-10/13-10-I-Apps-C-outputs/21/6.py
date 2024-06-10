
def count_non_equivalence_relations(n):
    def power_set(s):
        return [[]] + [s[:i] + [s[i]] + s[i+1:] for i in range(len(s))]
    
    def is_symmetric(relation):
        return all(relation[i][1] == relation[i][0] for i in range(len(relation)))
    
    def is_transitive(relation):
        return all(relation[i][1] in relation[i][0] for i in range(len(relation)))
    
    def is_non_equivalence(relation):
        return is_symmetric(relation) and is_transitive(relation) and not is_reflexive(relation)
    
    def is_reflexive(relation):
        return any(relation[i][0] == relation[i][1] for i in range(len(relation)))
    
    def count_non_equivalence_relations_helper(n, relation):
        if n == 0:
            if is_non_equivalence(relation):
                return 1
            else:
                return 0
        else:
            count = 0
            for i in range(n):
                for j in range(i+1, n):
                    relation.append([i, j])
                    count += count_non_equivalence_relations_helper(n-1, relation)
                    relation.pop()
            return count
    
    return count_non_equivalence_relations_helper(n, []) % (10**9 + 7)
    
if __name__ == '__main__':
    n = int(input())
    print(count_non_equivalence_relations(n))

