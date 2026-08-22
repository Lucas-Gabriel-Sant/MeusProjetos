word = ''
loop = 'S'
no_letters = ['']
import os
import re

def repeat():
    for t in range(0, 3):
        loop = input('Jogar novamente? ').upper()
        if loop[0] in 'SN':
            break
    if loop[0] not in 'SN':
        loop = 'N'
        print('Tentativas excedidas!')
    return loop

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def accentuation(w):
    n_w = re.sub(r'[áàâã]', 'a', w)
    n_w = re.sub(r'[éê]', 'e', n_w)
    n_w = n_w.replace('í', 'i').replace('ú', 'u').replace('ó', 'o')
    return n_w

def verify(test_letter):
    changes = 0
    global unk_word
    global errors
    global no_letters
    n_w = list(unk_word)
    for i, l in enumerate(test_word):
        if l == test_letter:
            n_w[i] = word[i]
            unk_word = ''.join(n_w)
            changes += 1
    if changes == 0:
        errors +=1
        no_letters.append(test_letter)

while loop[0] != 'N':
    word = input('Defina a palavra: ').strip()
    clear()

    test_word = accentuation(word.lower())

    raw_word = ''.join([l for l in word if l not in ' -'])

    errors = 0
    unk_word = re.sub(r'[{}]'.format(raw_word), '_', word)

    while unk_word != word:

        letter = ''
        while letter in no_letters:
            print(f"""Letras erradas: {no_letters}
            ___
            | '   {unk_word}""")
            letter = input('Seu chute: ').lower().strip()
            clear()
        verify(letter)

        if errors == 6:
            print('DERROTA!')
            break

    if unk_word == word:
       print('VITÓRIA!')

    loop = repeat()
    clear()