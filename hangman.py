import random

path= "/usr/share/dict/words"

def get_random_word(path):
    words=list(open(path))
    rand_word=[]

    for word in words:
        word=word.strip()
        if  not word.isalpha():
            continue
        if len(word) < 6:
            continue
        if word[0].isupper():
            continue
        rand_word.append(word)

    return random.choice(rand_word)
    
def hidden_word (word,guess_char):
    hiden_word= ''
    for letter in word: 
        if letter in guess_char:
            hiden_word += letter
        else:
            hiden_word += '-'
    return hiden_word


def get_status(secret_word, guesses, turns_left):
    masked_word = hidden_word(secret_word, guesses)
    return f"""Word : {masked_word}
Turns left : {turns_left}"""

def evaluate_input(secret_word, guesses, turns_left, input_):
    if input_ in guesses:
        return f"You already guessed '{input_}'", turns_left
    
    if "-" not in hidden_word(secret_word, guesses+[input_]):
        return "word has been guessed", turns_left

    if input_ in secret_word:
        guesses.append(input_)
        return "good guess", turns_left

    if input_ not in secret_word:
        if turns_left == 1:
            return "game is over", turns_left
        else:
            guesses.append(input_)
            return "bad guess", turns_left - 1

def hangman():
    secret_word = get_random_word(path)
    print (secret_word)
    guesses = []
    turns_left = 7
    status = ""
    while status not in ["word has been guessed", "game is over"]:
        print ("\n", status)
        print (get_status(secret_word, guesses, turns_left))
        guess = input("Enter a letter ")
        print (f'"{guess}"')
        status, turns_left = evaluate_input(secret_word, guesses, turns_left, guess)

if __name__ == "__main__":
    hangman()

        