from collections import deque 
import copy

# Complete the function below
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

def neighbors(sequence1, sequence2 ):
    num_differences=0
    for a,b in zip(sequence1,sequence2):
        if a != b:
            num_differences += 1
            
    if num_differences == 1:
        return 1
    else:
        return 0

def  findMutationDistance(start, end, bank):
    
    if is_valid_DNA(start, end, bank) and is_valid_Mutation(end, bank):
        
        paths = deque([[str(start)]])
        solutions = deque([])
        dumpList = [str(start)]
        
        while (len(paths) > 0):
            for sequence in bank:
                if neighbors(sequence, paths[0][0]) and sequence not in dumpList:
                    if sequence == end:
                        paths[0].insert(0,end)
                        new_solution = copy.deepcopy(paths[0])
                        solutions.append(new_solution)
                        paths.popleft()
                        break
                    else:
                        new_path = copy.deepcopy(paths[0])
                        new_path.insert(0,sequence)
                        paths.append(new_path)
                        dumpList.append(sequence)
            if len(paths) > 0:
                paths.popleft()
                
        if len(solutions) == 0:
            return -1
        else:
            path_lengths = [len(i) for i in solutions]
            return min(path_lengths)-1
        
        
    else:
        return -1