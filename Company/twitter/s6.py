from collections import deque

def is_valid_DNA(start, end, bank):
    bank.extend((start,end))
    
    # Check length of each sequence = 8                
    for sequence in bank:
        if len(sequence) != 8:
            return 0
     
    # Check each sequence contains allowed nucleotides
    allowed_nucleotides = ['A','C','T','G']
    for sequence in bank:
        for nucleotide in sequence:
            if nucleotide not in allowed_nucleotides:
                return 0
    
    return 1

def is_valid_Mutation(end,bank):
    if end in bank:
        return 1
    else:
        return 0

def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
def bfs_words(begin, end, dict_words):
    queue, visited = deque([(begin, 1)]), set()
    while queue:
        word, steps = queue.popleft()
        if word not in visited:
            visited.add(word)
            if word == end:
                return steps
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                neigh_words = dict_words.get(s, [])
                for neigh in neigh_words:
                    if neigh not in visited:
                        queue.append((neigh, steps + 1))
    return 0
    
def  findMutationDistance(start, end, bank):
    
    if is_valid_DNA(start, end, bank) and is_valid_Mutation(end, bank):
        
        d = construct_dict(bank)
        return bfs_words(start, end, d) -1
        
    else:
        return -1