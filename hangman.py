import random

def get_random_word(path= "/usr/share/dict/words"):
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
    
def hide_word (word,guess_char):
    hiden_word= ''
    for letter in word: 
        if letter in guess_char:
            hiden_word += letter
        else:
            hiden_word += '-'
    return hiden_word


def get_status(secret_word, guesses, turns_left):
    return f"""Word : {hide_word(secret_word, guesses)}
Turns left : {turns_left}"""


def process_input(secret_word, guesses, turns_left, input_):
    if input_ in guesses:
        return f"YOU ALREADY GUESSED '{input_}'", turns_left
    
    elif "-" not in hide_word(secret_word, guesses+[input_]):
        print('you win man!')
        return "YOU WIN", turns_left
    
    elif turns_left == 1:
        print('HA HA! you lose buddy :)')
        return "YOU LOSE", turns_left 

    elif input_ in secret_word:
        guesses.append(input_)
        return "NICE TRY", turns_left

    #elif input_ not in secret_word:

    else:
        guesses.append(input_)
        return "OOPS! TRY MORE", turns_left - 1

def main():
    secret_word = get_random_word()
    print (secret_word)
    guesses = []
    turns_left = 7
    status = ""
    while status not in ["YOU WIN", "YOU LOSE"]:
        print ("\n", status)
        print (get_status(secret_word, guesses, turns_left))
        guess = input("Guess a letter:").lower()
       # print (f'"{guess}"')
        status, turns_left = process_input(secret_word, guesses, turns_left, guess)

if __name__ == "__main__":
    main()