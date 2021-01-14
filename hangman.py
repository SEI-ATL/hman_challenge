words = ['what', 'is', 'the', 'secret', 'word', 'kristin', 'wiig']
secret_word = words[5]

def hash(string):
    length = len(string)
    hash = "_" * length
    return hash

hashed = hash(secret_word)

def check_word(l):
    secret_word_list = [char for char in secret_word]
    to_reveal = []
    for i in range(len(secret_word_list)):
        if l == secret_word_list[i]:
            new = hashed[:i] + secret_word[i] + hashed[i:]
            new_hashed = new[:-1]
    if 
    return new_hashed

letter = input('Enter a letter: ')
print(check_word(letter))
