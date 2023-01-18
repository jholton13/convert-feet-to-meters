#the game
def main():
    playerone = input('Player 1: Enter R for rock, P for paper, or S for scissors:')
    playertwo = input('Player 2: Enter R for rock, P for paper, or S for scissors:')

#player entries
    symbol = [playerone.upper(), playertwo.upper()]

#same entries
    if symbol[0] == symbol[1]:
        print('It is a tie')

#rock and paper
    elif symbol == ['R', 'P'] or symbol == ['P', 'R']:
        if symbol[0] == 'P':
            print('Player 1 has won the game!')
        else:
            print('Player 2 has won the game!')

#rock and scissor
    elif symbol == ['R', 'S'] or symbol == ['S', 'R']:
        if symbol[0] == 'R':
            print('Player 1 has won the game!')
        else:
            print('Player 2 has won the game!')

#scissor and paper
    elif symbol == ['S', 'P'] or symbol == ['P', 'S']:
        if symbol[0] == 'S':
            print('Player 1 has won the game!')
        else:
            print('Player 2 has won the game!')

#invalid
        print('Game canceled because of invalid entry.')

#call function
main();

