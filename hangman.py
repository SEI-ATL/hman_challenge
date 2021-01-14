# import Mongo
from pymongo import MongoClient
client = MongoClient()
db = client.test_database

hman_challenge = requests.get('hangman-api')
# words = ['what', 'is', 'the', 'secret', 'word', 'kristin', 'wiig']
# hman_challenge.json.get(word)

words = {
    'choices': hman_challenge.json.get(word_list)
    'userchoice': []
}

word_index = random.randint(0, len(words))
secret_word = words[choices[word_index]]

def hash(string):
    length = len(string)
    hash = "_" * length
    return hash

hashed = hash(secret_word)

def check_word(l, word):
    secret_word_list = [char for char in word]
    to_reveal = []
    for i in range(len(secret_word_list)):
        if l == secret_word_list[i]:
            to_reveal.append(i)
    for i in range(len(to_reveal)):
        index = to_reveal[i]
        new = hashed[:index] + secret_word[index] + hashed[index:]
        new_hashed = new[:-1]
    if len(to_reveal) == 0:
        return 'Not found!'

    return new_hashed

letter = input('Enter a letter: ')
# counter for turns: the length of the word
def turns()
check_word(letter, secret_word)
