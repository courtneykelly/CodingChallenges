from collections import defaultdict
from itertools import product
import os


def build_graph(words):
    buckets = defaultdict(list)
    graph = defaultdict(set)

    for word in words:
        for i in range(len(word)):
            bucket = '{}_{}'.format(word[:i], word[i + 1:])
            buckets[bucket].append(word)

    # add vertices and edges for words in the same bucket
    for bucket, mutual_neighbors in buckets.items():
        for word1, word2 in product(mutual_neighbors, repeat=2):
            if word1 != word2:
                graph[word1].add(word2)
                graph[word2].add(word1)

    return graph



word_graph = build_graph(['AAAAAAAA', 'AAAAAAAT', 'AAAAAATT', 'AAAAATTT'])
print word_graph
# word_graph['FOOL']
# set(['POOL', 'WOOL', 'FOWL', 'FOAL', 'FOUL', ... ])