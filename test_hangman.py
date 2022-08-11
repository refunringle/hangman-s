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
    assert hangman.hide_word(my_word,[]) == '--------'
    assert hangman.hide_word(my_word,['e']) == 'e-e-----'
    assert hangman.hide_word(my_word,['e','a']) == 'e-e--a--'
    assert hangman.hide_word(my_word,['e','a','x']) == 'e-e--a--'

def test_mark_word_invalid_guesses():
    for i in ["police", "elephant", "it", "foo"]:
        assert hangman.hide_word(i, ["x", "q"]) == len(i)*"-"


def test_get_status():
    secret_word = "itsrefun"
    guesses = ['n', 'i', 'p', 'a']
    status = hangman.get_status(secret_word, guesses, 5)
    assert status == f"""Word : i------n
Turns left : 5"""


def test_evaluate_input_word_guessed():
    secret_word = "red"
    guesses = ["e", "a", "d", "m"]
    turns_left = 5
    input_ = "r"
    resp, turns_left = hangman.process_input(secret_word, guesses, turns_left, input_)
    assert turns_left == 5
    assert resp == "YOU WIN"
    
def test_evaluate_input_bad_guess():
    secret_word = "black"
    guesses = ["b", "a", "x", "m"]
    turns_left = 5
    input_ = "q"
    resp, turns_left = hangman.process_input(secret_word, guesses, turns_left, input_)
    assert resp == "OOPS! TRY MORE"
    assert guesses == ["b", "a", "x", "m", "q"]
    assert turns_left == 4

    
def test_evaluate_input_game_over():
    secret_word = "pink"
    guesses = ["c", "i", "x", "k"]
    turns_left = 1
    input_ = "q"
    resp, _ = hangman.process_input(secret_word, guesses, turns_left, input_)
    assert resp == "YOU LOSE"

def test_evaluate_input_repeat_guess():
    secret_word = "yellow"
    guesses = ["c", "y", "o", "m"]
    turns_left = 5
    input_ = "c"
    resp, turns_left = hangman.process_input(secret_word, guesses, turns_left, input_)
    assert turns_left == 5
    assert resp == "YOU ALREADY GUESSED 'c'"

def test_evaluate_input_good_guess():
    secret_word = "blue"
    guesses = ["e", "u", "m"]
    turns_left = 5
    input_ = "b"
    resp, turns_left = hangman.process_input(secret_word, guesses, turns_left, input_)
    assert resp == "NICE TRY"
    assert turns_left == 5
