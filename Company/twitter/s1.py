

def wordLadder(start, finish):
    possibleWords = [pw.strip() for pw in open('words.txt').readlines()]
    currentWords = [[[start]]]

    while True:
        currentWords.append([currentWord + [possibleWord] for currentWord in currentWords[-1] for possibleWord in possibleWords if len(filter(lambda x: possibleWord[x]!=currentWord[-1][x], range(len(currentWord[-1])))) == 1])
        for word in currentWords[-1]:
            if word[-1] == finish: return word

print wordLadder('leap', 'look')

