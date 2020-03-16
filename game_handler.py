from board_class import board
from codemaker import code_maker
from codebreaker import code_breaker

#Parameters to be set before game
possible_colours=['White','Light_Blue','Green','Orange','Red','Dark_Blue','Black','Yellow']
no_of_rounds=10
with_blanks=False

if(with_blanks):
	possible_colours.append('Blank')

player1=code_maker(possible_colours)
player2=code_breaker(possible_colours)
game_board=board(player1.code,player2.set_of_codes)
game_board.response.append(player1.response(game_board.codebreaker_code[-1]))
no_of_rounds-=1

while(no_of_rounds>0):
	game_board.codebreaker_code.append(player2.solve(game_board.response[-1])) #Player2 plays next move
	game_board.response.append(player1.response(game_board.codebreaker_code[-1])) #Player1 checks player2's move and return response
	if(game_board.end_game()):
		break
	game_board.print_board()
	no_of_rounds-=1

if(no_of_rounds>0):
	print('Player 2 won!')
else:
	print('Player 1 won!')



