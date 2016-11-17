from string import ascii_lowercase as chars
from heapq import heappush, heappop

def a_star(G, s, t, h):
	P, Q = {}, [(h(s), None, s)] # Preds and queue w/heuristic
	while Q: # Still unprocessed nodes?
		d, p, u = heappop(Q) # Node with lowest heuristic
		if u in P: continue # Already visited? Skip it
		P[u] = p # Set path predecessor
		if u == t: return d - h(t), P # Arrived! Ret. dist and preds
		for v in G[u]: # Go through all neighbors
			w = G[u][v] - h(u) + h(v) # Modify weight wrt heuristic
			heappush(Q, (d + w, u, v)) # Add to queue, w/heur as pri
	return float('inf'), None # Didn't get to t

class WordSpace: # An implicit graph w/utils
	def __init__(self, words): # Create graph over the words
		self.words = words
		self.M = M = dict() # Reachable words

	def variants(self, wd, words): # Yield all word variants
		wasl = list(wd) # The word as a list
		for i, c in enumerate(wasl): # Each position and character
			for oc in chars: # Every possible character
				if c == oc: continue # Don't replace with the same
				wasl[i] = oc # Replace the character
				ow = ''.join(wasl) # Make a string of the word
				if ow in words: # Is it a valid word?
					yield ow # Then we yield it
			wasl[i] = c # Reset the character

	def __getitem__(self, wd): # The adjacency map interface
		if wd not in self.M: # Cache the neighbors
			self.M[wd] = dict.fromkeys(self.variants(wd, self.words), 1)
		return self.M[wd]

	def heuristic(self, u, v): # The default heuristic
		return sum(a!=b for a, b in zip(u, v)) # How many characters differ?

	def ladder(self, s, t, h=None): # Utility wrapper for a_star
		if h is None: # Allows other heuristics
			def h(v):
				return self.heuristic(v, t)
		_, P = a_star(self, s, t, h) # Get the predecessor map
		if P is None:
			return [s, None, t] # When no path exists
		u, p = t, []
		while u is not None: # Walk backward from t
			p.append(u) # Append every predecessor
			u = P[u] # Take another step
		p.reverse() # The path is backward
		return p

if __name__ == '__main__':
	G = WordSpace(['GAAAAAAA', 'AAGAAAAA', 'AAAAGAAA', 'GGAAAAAA'])
	print G.ladder('AAAAAAAA', 'GGAAAATT')