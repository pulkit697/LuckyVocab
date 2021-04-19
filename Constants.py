import random

SERVER_IP = 'localhost'
ENCODING_METHOD = 'utf-8'
SERVER_PORT = 9999
DATA_RECEIVED = 'DATA_RECEIVED'
words = ["gradually", "phrase", "future", "increase", "customs", "spell", "see", "draw", "butter", "brown", "order",
         "solid", "beginning", "rear", "smell", "plates", "article", "buffalo", "traffic", "swim", "clear", "active",
         "wherever", "loss", "source", "themselves", "arrangement", "question", "fire", "gather", "claws", "thin",
         "wish", "tone", "carried", "stove", "first", "slightly", "opinion", "land", "development", "crop", "stairs",
         "acres", "few", "simple", "travel", "personal", "piano", "street", "anyway", "suppose", "fog", "coast", "cool",
         "earn", "monkey", "trick", "curve", "conversation", "flag", "practical", "today", "pitch", "rising", "red",
         "about", "ordinary", "teeth", "flew", "deer", "prevent", "happy", "fat", "stream", "whale", "tonight", "wheat",
         "appropriate", "therefore", "treated", "anyone", "verb", "read", "gasoline", "drew", "easy", "surprise",
         "dead", "compass", "putting", "plate", "lift", "lying", "composition", "model", "certain", "shop", "border",
         "direction", "sit", "skill", "pleasure", "printed", "dull", "remember", "pupil", "bear", "badly", "rush",
         "chain", "greatly", "happily", "beyond", "electricity", "corn", "thing", "moving", "occur", "wheel", "writer",
         "stiff", "solve", "these", "baseball", "noise", "love", "correct", "beginning", "thumb", "poetry", "also",
         "difference", "have", "full", "sudden", "felt", "put", "satellites", "solid", "getting", "vast", "arrangement",
         "pig", "energy", "whenever", "won", "excited", "without", "atomic", "missing", "repeat", "clock", "changing",
         "been", "apple", "length", "hearing", "length", "spread", "send", "generally", "getting", "weather", "globe",
         "hot", "wheel", "ever", "dot", "consist", "floating", "funny", "government", "double", "dead", "create",
         "feed", "measure", "likely", "forgot", "bigger", "orbit", "frighten", "loud", "hurry", "rapidly"]
NUMBER_OF_ROUNDS = 2
FLAG_RESPONSE_SUBMITTED = 'FLAG_RESPONSE_SUBMITTED'
FLAG_ALL_SUBMISSIONS_RECEIVED = 'FLAG_ALL_SUBMISSIONS_RECEIVED'

def calculate_difference(word1, word2):
    score = 10
    if len(word1) == len(word2):
        for i in range(len(word1) - 1):
            if word1[i] == word2[i]:
                score += 5
    return score


def return_blank_string(_word, count):
    to_be_returned = ''
    indices = set()
    while len(indices) < count:
        indices.add(random.randint(0, len(_word) - 1))
    for i in range(len(_word)):
        if i in indices:
            to_be_returned += '_'
        else:
            to_be_returned += _word[i]
    return to_be_returned


def choose_random_word():
    return words[random.randint(0, len(words) - 1)]
