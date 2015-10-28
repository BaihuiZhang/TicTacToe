'''This is the main file for the Tic Tac Toe function
	And all the comments are put in here!
'''

#To draw a 3*3 board
board = []
for x in range(0,3):
	board.append(["|_|"] * 3)

def print_board(board):
	for row in board:
		print (" ".join(row))

print_board(board)


for turn in range(9):
	print ("Turn", turn + 1)	
	#Get inputs of the player's move
	inputpos = int(input("Please input the your next move(1-9,left to right,up to down):"))
	print ("Your move is %s" % input)
	if inputpos <= 3:
		board[0][inputpos-1] = "|X|"
	elif inputpos <= 6:
		board[1][inputpos-4] = "|X|"
	elif inputpos <= 9:
		board[2][inputpos-7] = "|X|"
	else:
		inputpos = int(inputpos("No such position, please input again"))	 
	print_board(board)



#Here write the method that determines the winning situation


#Here write the computer's AI

