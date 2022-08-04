import random

import hangman

random.seed(8)

def test_get_random_word_min_length_6():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['ambulances', 'cat', 'car', 'dog', "hen"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "ambulances"

def test_get_random_word_no_non_alphanum():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['elephants', "hospital's", "policeman's"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "elephants"

def test_get_random_word_no_proper_noun():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['firehouse', "Abraham", "Mercury"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "firehouse"


def test_get_random_word():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['ambulances', 'hospitalized', 'car', 'Abraham', "mercury's"]:
            f.write(i+"\n")
    words = set()
    for _ in range(8):
        word = hangman.get_random_word(my_dict)
        print (word)
        words.add(word)
    assert words == {"hospitalized", 'ambulances'}

def test_get_secret_word():
    my_word ='elephant'
    assert hangman.find_sentence(my_word,[]) == '--------'
    assert hangman.find_sentence(my_word,['e']) == 'e-e-----'
    assert hangman.find_sentence(my_word,['e','a']) == 'e-e--a--'
    assert hangman.find_sentence(my_word,['e','a','x']) == 'e-e--a--'

def test_mark_word_invalid_guesses():
    for i in ["police", "elephant", "it", "foo"]:
        assert hangman.find_sentence(i, ["x", "q"]) == len(i)*"-"


