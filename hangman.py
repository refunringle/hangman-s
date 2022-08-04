import random

path= "/usr/share/dict/words"

def get_random_word(path):
    words=list(open(path))
    rand_word=[]

    for word in words:
        word=word.strip()
        if  not word.isalpha():
            continue
        if len(word) < 7:
            continue
        if word[0].isupper():
            continue
        rand_word.append(word)

    return random.choice(rand_word)
    
def find_sentence (word,guess_char):
    hiden_word= ''
    for letter in word: 
        if letter in guess_char:
            hiden_word += letter
        else:
            hiden_word += '-'
    return hiden_word
