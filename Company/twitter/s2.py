from collections import defaultdict

def get_pseudos(word):
    return [word[:i] + '?' + word[i+1:] for i in range(len(word))]

def get_path(start, dest):
    chains = [ [start] ]
    while True:
        new_chains = []
        for chain in chains:
            # if the last word in the chain is the destination we're done, return the chain
            if chain[-1] == dest:
                return chain
            else:
                # otherwise, add another link to the chains
                for pseudo_word in get_pseudos(chain[-1]):
                    for word in conns[pseudo_word]:
                        if word != chain[-1]:
                            new_chains.append( chain + [word] )

        chains = new_chains

if __name__ == "__main__":
    with open('wl.txt') as f:
        words = [word.strip() for word in f]

    # create a mapping for a "pseudoword" like co?k to real words e.g., 
    #   co?k => [ cork, cook, conk, ... ]
    # also, we're using sets, so we won't see any duplicate words
    conns = defaultdict(set)
    for word in words:
        for pseudo_word in get_pseudos(word):
            conns[pseudo_word].add(word)

    word = "look"
    dest = "leap"

    print get_path(word, dest)