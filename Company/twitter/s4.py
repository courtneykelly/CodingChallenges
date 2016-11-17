from collections import defaultdict

def get_possible_sequences(word):
	return [word[:i] + '?' + word[i+1:] for i in range(len(word))]

def add_word(word, data):
    for g in get_possible_sequences(word):
        data[g].add(word)

def get_connections(word, data):
    l = set()
    for sequence in get_possible_sequences(word):
        l |= data[sequence]
    l.remove(word) # exclude the word itself
    return l

def get_shortest_path(start, end, maps):
	used = get_connections(start, maps)
	used.add(start)
	paths = [ (start,x) for x in get_connections(start,maps) ]
	while True:
		path = paths.pop(0)
		if path[-1] == end:
			return list(path)
		paths.extend(path + (x,) for x in get_connections(path[-1], maps) - used)

def  findMutationDistance(start, end, bank):

	maps = defaultdict(set)
	for sequence in bank:
		add_word(sequence, maps)

	return len(get_shortest_path(start, end, maps)) - 1

print findMutationDistance('AAAAAAAA', 'AAAAAATT', ['AAAAAAAA', 'AAAAAAAT', 'AAAAAATT', 'AAAAATTT'])