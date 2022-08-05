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
    assert hangman.hidden_word(my_word,[]) == '--------'
    assert hangman.hidden_word(my_word,['e']) == 'e-e-----'
    assert hangman.hidden_word(my_word,['e','a']) == 'e-e--a--'
    assert hangman.hidden_word(my_word,['e','a','x']) == 'e-e--a--'

def test_mark_word_invalid_guesses():
    for i in ["police", "elephant", "it", "foo"]:
        assert hangman.hidden_word(i, ["x", "q"]) == len(i)*"-"


def test_get_status():
    secret_word = "aeroplane"
    guesses = ['x', 't', 'p', 'a']
    status = hangman.get_status(secret_word, guesses, 5)
    assert status == f"""Word : a---p-a--
Turns left : 5"""


def test_evaluate_input_word_guessed():
    secret_word = "cat"
    guesses = ["c", "a", "x", "m"]
    turns_left = 5
    input_ = "t"
    resp, turns_left = hangman.evaluate_input(secret_word, guesses, turns_left, input_)
    assert turns_left == 5
    assert resp == "word has been guessed"
    
def test_evaluate_input_bad_guess():
    secret_word = "cat"
    guesses = ["c", "a", "x", "m"]
    turns_left = 5
    input_ = "q"
    resp, turns_left = hangman.evaluate_input(secret_word, guesses, turns_left, input_)
    assert resp == "bad guess"
    assert guesses == ["c", "a", "x", "m", "q"]
    assert turns_left == 4

    
def test_evaluate_input_game_over():
    secret_word = "cat"
    guesses = ["c", "a", "x", "m"]
    turns_left = 1
    input_ = "q"
    resp, _ = hangman.evaluate_input(secret_word, guesses, turns_left, input_)
    assert resp == "game is over"

def test_evaluate_input_repeat_guess():
    secret_word = "cat"
    guesses = ["c", "a", "x", "m"]
    turns_left = 5
    input_ = "c"
    resp, turns_left = hangman.evaluate_input(secret_word, guesses, turns_left, input_)
    assert turns_left == 5
    assert resp == "You already guessed 'c'"

def test_evaluate_input_good_guess():
    secret_word = "cat"
    guesses = ["c", "x", "m"]
    turns_left = 5
    input_ = "a"
    resp, turns_left = hangman.evaluate_input(secret_word, guesses, turns_left, input_)
    assert resp == "good guess"
    assert turns_left == 5


    


