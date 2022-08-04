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
    
def find_sentence (word,epty):
    hiden_word= ''
    for c in word: 
        if c in epty:
            hiden_word += c
        else:
            hiden_word += '-'
    return hiden_word
