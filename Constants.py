import random
import socket

# SERVER_IP = "192.168.0.8"
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
# colors
FRAME1_BG_COLOR = 'white'
FRAME2_BG_COLOR = 'white'
FRAME3_BG_COLOR = 'white'
HOST_BG_COLOR = 'white'
PARTICIPANTS_BG_COLOR = 'white'
EXIT_BUTTON_BG_COLOR = 'blue'
EXIT_BUTTON_BG_COLOR_ACTIVATED = 'blue'
EXIT_BUTTON_FG_COLOR = 'white'
EXIT_BUTTON_FG_COLOR_ACTIVATED = 'white'
ROUND_NUMBER_TEXT_COLOR = 'black'
ROUND_NUMBER_BG_COLOR = 'white'
QUERY_STRING_FG_COLOR = 'black'
QUERY_STRING_BG_COLOR = 'white'
CORRECT_ANSWER_FG_COLOR = 'GREEN'
CORRECT_ANSWER_BG_COLOR = 'WHITE'
CORRECT_ANSWER_FONT = ('roboto', 12)
TEXT_INPUT_RESPONSE_FG_COLOR = 'BLACK'
TEXT_INPUT_RESPONSE_BG_COLOR = 'WHITE'
TEXT_INPUT_RESPONSE_CURSOR_COLOR = 'grey'
TEXT_INPUT_RESPONSE_FONT = ('Fira code', 10)
TIMER_BG_COLOR = 'white'
TIMER_FG_COLOR = 'black'
QUERY_STRING_TEXT_SIZE = 20
QUERY_STRING_FONT = ('fira code', 12)
RESULT_WINNER_FONT = ('fire code', 10)


def calculate_difference(word1, word2):
    score = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
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
