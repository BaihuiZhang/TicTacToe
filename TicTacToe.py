'''This is the main file for the Tic Tac Toe function
	And all the comments are put in here!
'''

#To draw a 3*3 board
board = []
for x in range(0,3):
	board.append(["|__|"] * 3)

def print_board(board):
	for row in board:
		print (" ".join(row))

print_board(board)


for turn in range(9):
	print ("Turn", turn + 1)	
	#Get inputs of the player's move
	input = int(input("Please input the your next move(1-9,left to right,up to down):"))
	print ("Your move is %s" % input)
	board[input-1] = "|x|"
	print_board(board)



#Here write the method that determines the winning situation


#Here write the computer's AI

