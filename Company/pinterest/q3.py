import json
import urllib
import urllib2
import operator
import itertools

ACCESS_TOKEN = 'AY5d3Zep5S-0PGUiCPrQmGBiwxmsFIQr4hqxJ01DiC0EOCBAsAAAAAA'

BASE_API = "https://api.pinterest.com"

NLTK_STOPWORDS = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']

def get_request(path, params=None):
    """
    Given a path, e.g. '/v1/me/' and params, return the response in json form.
    Take a look at https://developers.pinterest.com/docs/getting-started/introduction/
    to see what endpoints the Pinterest API has available!

    You may request additional parameters by overriding the params method
    """
    if params:
        params.update({'access_token': ACCESS_TOKEN})
    else:
        params = {'access_token': ACCESS_TOKEN}
    url = "%s%s?%s" % (BASE_API, path, urllib.urlencode(params))
    result = urllib2.urlopen(url)
    response_data = result.read()
    return json.loads(response_data)

def is_word(word):

    # word must be a minimum of 2 letters
    if len(word) < 2:
        return False

    # word must only contain ASCII characters that are the alphabet, ' , or -
    exceptions = ["=", "'"] 
    for letter in word:
        if not letter.isalpha() and letter not in exceptions:
            return False

    # word must not be in nltk's stopwords
    if word in NLTK_STOPWORDS:
        return False

    return True

def top_n_words(board_id, top_N):
    
    # set parameters & path for API request
    params = {'limit': 100, 'fields': 'note'}
    path = '/v1/boards/%d/pins/' % board_id
    data = get_request(path, params)

    # create dictionary to store words from the retrieved notes
    notes = dict()

    # 1. First we loop through retrieved data, and iterate over key, value pairs.
    # 2. Then, we must make sure key is of type 'note' bc both note and id are 
    #    returned to the data variable by the API
    # 3. Then we iterate over each word in the note, utilizing the split() function
    # 4. Finally, we only add word to the dictionary notes if it meets the
    #    requirements outlined by the is_word() function
    for data in data['data']:
        for key, value in data.iteritems(): 
            if key == 'note':  
                for word in value.split(): 
                    if is_word(word):   
                        notes[word] = notes.get(word,0) + 1

    # sort the dictionary in descending order
    sorted_notes = sorted(notes.items(), key=operator.itemgetter(1), reverse=True)

    # list of final notes, later converted to a set
    final_notes = []

    # print notes with upper limit of top_N and store the value of the last note
    for note in itertools.islice(sorted_notes, top_N):
        new_tuple = (note[0].lower(),note[1])
        final_notes.insert( len(final_notes), new_tuple )
        value = note[1]

    # print the notes following the last note if they have the same count 
    # it's a tie!
    for note in itertools.islice(sorted_notes, top_N, None):
        if note[1] == value:
            new_tuple = (note[0].lower(),note[1])
            final_notes.insert( len(final_notes), new_tuple )

    return set(final_notes)

print top_n_words(785174584973334870, 1)