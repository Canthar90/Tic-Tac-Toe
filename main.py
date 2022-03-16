





game_list_x = []
game_list_o = []
play_game = True
last_one = ''

def drawning(marker, positions_x, positions_o):
    form_list = [' ', '|', ' ', '|', ' ']
    drawning = ''
    for row in range(0, 3):

        if f'{row}.1' in positions_x:
            drawning +='\n' + ' ' + 'X' + ' ' + '|'
        elif f'{row}.1' in positions_o:
            drawning += '\n' + ' ' + 'O' + ' ' + '|'
        else:
            drawning +='\n' + ' ' + ' ' + ' ' + '|'

        if f'{row}.2' in positions_x:
            drawning += ' ' + 'X' + ' '
        elif f'{row}.2' in positions_o:
            drawning += ' ' + 'O' + ' '
        else:
            drawning += ' ' + ' ' + ' '

        if f'{row}.3' in positions_x:
            drawning += '|' + ' ' + 'X' + ' '
        elif f'{row}.3' in positions_o:
            drawning += '|' + ' ' + 'O' + ' '
        else:
            drawning += '|' + ' ' + ' ' + ' '

        if row != 3:
            drawning += '\n-----------'

    print(drawning)
    pass



def is_it_the_end(score_x, score_o):

    if len(score_x)+len(score_o) >= 9:
        print("We have a Draw !!!!")
        return True
    elif ('0.1' and '1.2' and '2.3') in score_x or ('0.1' and '1.1' and '2.1') in score_x or ('0.1' and '0.2' and '0.3') in score_x or ('0.3' and '1.2' and '2.1') in score_x \
            or ('1.1' and '1.2' and '1.3') in score_x or ('2.1' and '2.2' and '2.3') in score_x:
        print("X Player Winss !!!!")
        return True

    elif ('0.1' and '1.2' and '2.3') in score_o or ('0.1' and '1.1' and '2.1') in score_o or ('0.1' and '0.2' and '0.3') in score_o or ('0.3' and '1.2' and '2.1') in score_o \
            or ('1.1' and '1.2' and '1.3') in score_o or ('2.1' and '2.2' and '2.3') in score_o:
        print("O Player Winss !!!!")
        return True
    return False
    pass

# print('-----------')

while play_game:
    print("This is tic tac toe game playing you should enter one of the positions 0.1 0.2 0.3 or 1.1 1.2 and so one")
    if last_one == 'X':
        choose = input('Plis chose the position of Your O choose')
        if choose in game_list_o or choose in game_list_x:
            print("Plis chose another place this was already taken")
        else:
            last_one = 'O'
            game_list_o.append(choose)
    elif last_one == 'O' or last_one == '':
        choose = input('Plis chose the position of Your X choose')
        if choose in game_list_o or choose in game_list_x:
            print("Plis chose another place this was already taken")
        else:
            game_list_x.append(choose)
            last_one = 'X'
    drawning(marker=last_one, positions_x=game_list_x, positions_o=game_list_o)
    you_know = is_it_the_end(score_x=game_list_x, score_o=game_list_o)
    if you_know:
        end = input("Do you wish to play again? print 'y' or 'n' : ").lower()
        if end == 'n':
            play_game = False
        elif end == 'y':
            last_one = ''
            game_list_x = []
            game_list_o = []

        else:
            print("Bad input exiting the game")
            play_game = False


