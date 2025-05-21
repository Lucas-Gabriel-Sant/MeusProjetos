"""Author: Lucas Gabriel Santos
Date: 09/04/2025
Version 1.1
a"""

import random

immutable_pack = ('4 de copas', '4 de ouros', '4 de espadas', '4 de paus',
'5 de copas', '5 de ouros', '5 de espadas', '5 de paus',
'6 de copas', '6 de ouros', '6 de espadas', '6 de paus',
'7 de copas', '7 de ouros', '7 de espadas', '7 de paus',
'10 de copas', '10 de ouros', '10 de espadas', '10 de paus',
'11 de copas', '11 de ouros', '11 de espadas', '11 de paus',
'12 de copas', '12 de ouros', '12 de espadas', '12 de paus',
'1 de copas', '1 de ouros', '1 de espadas', '1 de paus',
'2 de copas', '2 de ouros', '2 de espadas', '2 de paus',
'3 de copas', '3 de ouros', '3 de espadas', '3 de paus')

pack = ['4 de copas', '4 de ouros', '4 de espadas', '4 de paus',
'5 de copas', '5 de ouros', '5 de espadas', '5 de paus',
'6 de copas', '6 de ouros', '6 de espadas', '6 de paus',
'7 de copas', '7 de ouros', '7 de espadas', '7 de paus',
'10 de copas', '10 de ouros', '10 de espadas', '10 de paus',
'11 de copas', '11 de ouros', '11 de espadas', '11 de paus',
'12 de copas', '12 de ouros', '12 de espadas', '12 de paus',
'1 de copas', '1 de ouros', '1 de espadas', '1 de paus',
'2 de copas', '2 de ouros', '2 de espadas', '2 de paus',
'3 de copas', '3 de ouros', '3 de espadas', '3 de paus']

value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

player_pontuation = 0
bot_pontuation = 0

def pick(quantity):
    cards = []
    for c in range(0, quantity):
        card = random.choice(pack)
        cards.append(card)
        pack.remove(card)
    return cards

def card_value(card):
    return value[immutable_pack.index(card)]

def comparation(player, bot):
    if card_value(player) > card_value(bot):
        return "Player wins"
    else:
        return "Bot wins"

"value[immutable_pack.index(player_play)]"

while True:
    players_deck = pick(3)
    bots_deck = pick(3)
    print(players_deck, bots_deck)
    for c in range(0, 3):
        player_play = random.choice(players_deck)
        players_deck.remove(player_play)
        bot_play = random.choice(bots_deck)
        bots_deck.remove(bot_play)
        print(player_play, bot_play)
        print(comparation(player_play, bot_play))
        if comparation(player_play, bot_play) == "Player wins":
            player_pontuation += 1
        else:
            bot_pontuation += 1
    break
print(player_pontuation, bot_pontuation)