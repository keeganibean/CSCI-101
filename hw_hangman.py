secret_word="test"
guessed_letters=""
def oldstyle(secret_word,guessed_letters):
    i=0
    letters=" "
    while i<len(secret_word):
        if secret_word[i] in guessed_letters:
            print('%s'%secret_word[i], end=' ')
        else:
            print('_',end=' ')
        i=i+1

secret_word="test"
guessed_letters=""
def newstyle(secret_word,guessed_letters):
    i=0
    letters=" "
    while i<len(secret_word):
        if secret_word[i] in guessed_letters:
            print('{}'.format(secret_word[i]), end=' ')
        else:
            print('_',end=' ')
        i=i+1

secret_word="test"
guessed_letters=""
def stringinterpolation(secret_word,guessed_letters):
    i=0
    letters=" "
    while i<len(secret_word):
        if secret_word[i] in guessed_letters:
            print(f'{secret_word[i]}', end=' ')
        else:
            print('_',end=' ')
        i=i+1
