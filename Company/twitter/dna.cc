#include <iostream>
#include <unordered_set>
#include <string>
    
using namespace std;

/*	Check if the passed DNA sequences are valid.
		- length = 8
		- only contain allowed nucleotides A,T,G,C
*/
bool is_valid_DNA( string start, string end, unordered_set<string> data, vector<char> nucleotides ) {
	data.insert(start);
	data.insert(end);

	for ( auto it = data.begin(); it != data.end(); it++ ) {
		string sequence = *it;
		if ( sequence.length() != 8 ) {
			return false;
		}
	}

	for ( auto itr = data.begin(); itr != data.end(); itr++ ) {
		string sequence = *itr;
		int length = sequence.length();
		for ( int c=0; c<length; c++ ) {
			char nucleotide = sequence[c];
			if ( find(nucleotides.begin(), nucleotides.end(), nucleotide) == nucleotides.end() ) {
				return false;
			}
		}
	}

	return true;


}

/*	Check if the proposed mutation is valid. If it is valid the end sequence
	will be in the bank.
*/
bool is_valid_mutation( string end, unordered_set<string> bank ) {

	if ( bank.find(end) == bank.end() ) {
		return false;
	}
	else {
		return true;
	}

}

/*	Find the mutation distance using BFS algorithm from two-ends. Start from the 
	start word and start from the end word. Once the start and end pointers reach 
	the same word, we are done. We can shorten the run time by creating two pointers, 
	one that points to the head, and another to the tail. Depending on the size of 
	the paths in head and tail, we can point phead to the smaller solution.
*/
int findMutationDistance(string start, string end, vector < string > v) {

    // convert bank to an unordered set
	unordered_set<string> bank(v.begin(), v.end());   

	// create 2 unordered sets, and two pointers to these objects
	unordered_set<string> head, tail, *phead, *ptail;

	// insert the start word into the head set, and the end word into the tail set
	head.insert(start);
	tail.insert(end);

	// initialize distance from start to end
	int distance = 2;
    
    // create a vector of the allowed nucleotides
	vector<char> nucleotides;
	nucleotides.push_back('A');
	nucleotides.push_back('T');
	nucleotides.push_back('G');
	nucleotides.push_back('C');

    // Check if valid mutation
	if (!is_valid_mutation(end, bank)) {
		return -1;
	}
    
    // Check if DNA is valid
	if (!is_valid_DNA(start, end, bank, nucleotides)) {
		return -1;
	}
    
	// like with normal BFS loop condition (while the set isn't empty), but we have to 
	// check both sets bc we are performing BFS from both ends
	while (!head.empty() && !tail.empty()) {
        
		// point phead to the smaller set
		// ptail provides the target word that head still needs to search for
		if (head.size() <= tail.size()) {
			phead = &head;
			ptail = &tail;
		}
		else {
			phead = &tail;
			ptail = &head;
		}

        // create temporary set and loop through unordered_set of value of phead
        // either head or tail depending on which is bigger
		unordered_set<string> temp;
		for ( auto it = phead->begin(); it != phead->end(); it++ ) {
			string sequence = *it;
			bank.erase(sequence);	// remove from set to avoid repeats = infinte loops
			int length = sequence.length();
            
            // loop through each nucleotide in DNA sequence 
			for ( int c=0; c<length; c++ ) {
				char nucleotide = sequence[c]; // save charactor to "put back" later
				
                // loop through allowed nucleotides and swap character for that nucleotide
                for ( auto itr = nucleotides.begin(); itr != nucleotides.end(); itr++ ) {
					sequence[c] = *itr;
                    
                    // if sequence is found in ptail, then head and tail have converged
                    // and we have found a solution!
					if ( ptail->find(sequence) != ptail->end() ) {
						return distance-1;    // return distance-1 bc don't count end in distance
					}
                    
                    // if sequence is found in the bank (valid change), then we can add
                    // add it to the temp set and erase from the bank
					if ( bank.find(sequence) != bank.end() ) {
						temp.insert(sequence);
						bank.erase(sequence);
					}
				}
				sequence[c] = nucleotide; // return seqeunce to orginal state
			}
		}
		distance++; // didn't find solution, added new sequence to set, so increase distance
		swap(*phead,temp); // temp is now the most up-to-date path to the solution, swap with the value of phead
	}

	return -1; // if all else fails, return -1
}

