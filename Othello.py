
import turtle
t = turtle.Turtle( )
s = turtle.Screen( )

def drawboard(n):
	t.hideturtle()
	t.speed("fastest")
	t.penup()
	t.goto(-200,200)
	t.pendown()
	t.goto(200,200)
	t.goto(200,-200)
	t.goto(-200,-200)
	t.goto(-200,200)
	for i in range(n):
		x_cor = 400/n
		t.forward(x_cor)
		t.sety(-200)
		t.sety(200)
	t.setheading(-90)
	for a in range(n):
		y_cor = 400/n
		t.forward(y_cor)
		t.setx(-200)
		t.setx(200)
	t.penup()
	t.goto(0,0)


def whichRow(y):
	for i in range(8):
		if (200-(50*(i))) > y > (200-(50*(i+1))):
			return i


def whichColumn(x):
	for i in range(8):
		if (-200+(50*(i))) < x < (-200+(50*(i+1))):
			return i

def xFromColumn(column):
	if column == 0:
		return -175
	if column == 1:
		return -125
	if column == 2:
		return -75
	if column == 3:
		return -25
	if column == 4:
		return 25
	if column == 5:
		return 75
	if column == 6:
		return 125
	if column == 7:
		return 175

def yFromRow(column):
	if column == 0:
		return 175
	if column == 1:
		return 125
	if column == 2:
		return 75
	if column == 3:
		return 25
	if column == 4:
		return -25
	if column == 5:
		return -75
	if column == 6:
		return -125
	if column == 7:
		return -175

def changePlayer(n):
	if n == 1:
		t.st()
		t.shape('circle')
		t.color('black')
	if n == 2:
		t.st()
		t.shape('circle')
		t.color('white')
		t.pencolor('black')

def stampPlayer(row, column, player):
	t.penup()
	changePlayer(player)
	t.goto(xFromColumn(column), yFromRow(row))
	t.stamp( )


gameboard = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

testboard =[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 'B', 'W', 0, 0, 0], [0, 0, 0, 'W', 'B', 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

def updateBoard(board, player, row, column):
	if player == 1:
		board[row][column] = 'B'
	else:
		board[row][column] = 'W'
	return board

def calculateScore(board, player):
	if player == 1:
		return sum([len(t) for t in [[h for h in a if h == 'B'] for a in board] if len(t)>0])
	else:
		return sum([len(t) for t in [[h for h in a if h == 'W'] for a in board] if len(t)>0])


def updateScore(board):
		t.goto(-275,275)
		t.pendown()
		t.write('Black')
		t.penup()
		t.goto(-275,240)
		t.dot(20,"white")
		t.pendown()
		t.write(calculateScore(board,1))
		t.penup()
		t.goto(275,275)
		t.pendown()
		t.write('White')
		t.penup()
		t.goto(275,240)
		t.dot(20,"white")
		t.pendown()
		t.write(calculateScore(board,2))
		t.penup()
		t.goto(400,-400)




def initialize():
	global turn
	drawboard(8)
	stampPlayer(3,3,1)
	stampPlayer(3,4,2)
	stampPlayer(4,4,1)
	stampPlayer(4,3,2)
	updateBoard(gameboard, 1, 3, 3)
	updateBoard(gameboard, 2, 3, 4)
	updateBoard(gameboard, 1, 4, 4)
	updateBoard(gameboard, 2, 4, 3)
	updateScore(gameboard)
	updateScore(gameboard)
	turn = 1

def validMove(board, player, row, column):
	if board[row][column] == 0:
		#if validMove_vert(board, player, row, column):
			#return True
		for a in [1, 0, -1]:
			for b in [1, 0, -1]:
				if a == 0 and b == 0:
					pass 
				else:
					if validMove_direct(board, player, row, column, a, b):
						return True
		return False
	else:
		return False


def validMove_direct(board, player, row, column, a, b): 
	if player == 1:
		if (row+a) > 7 or (column+b) > 7 or (row+a) < 0 or (column+b) < 0:
			return False
		else:
			if board[row+a][column+b] == 'W':
				if (row+(2*a)) > 7 or (column+(2*b)) > 7 or (row+(2*a)) < 0 or (column+(2*b)) < 0:
					return False
				elif board[row+(2*a)][column+(2*b)] == 'B':
					return True
				elif board[row+(2*a)][column+(2*b)] == 'W':
					return validMove_direct(board, player, row+a, column+b, a, b)
				else:
					return False
	else: 
		if (row+a) > 7 or (column+b) > 7 or (row+a) < 0 or (column+b) < 0:
			return False
		else:
			if board[(row+a)][(column+b)] == 'B':
				if (row+(2*a)) > 7 or (column+(2*b)) > 7 or (row+(2*a)) < 0 or (column+(2*b)) < 0:
					return False
				elif board[row+(2*a)][column+(2*b)] == 'W':
					return True
				elif board[row+(2*a)][column+(2*b)] == 'B':
					return validMove_direct(board, player, row+a, column+b, a, b)
				else:
					return False
'''
def validMove_vert(board, player, row, column):
	if player == 1:
			if (row+1) > 7 or (column) > 7 or (row+1) < 0 or (column) < 0:
					return False
			else:
				if board[row+1][column] == 'W':
					if (row+1) > 7 or (column) > 7 or (row+1) < 0 or (column) < 0:
						return False
					elif board[row+(2)][column] == 'B':
						return True
					elif board[row+(2)][column] == 'W':
						return validMove_vert(board, player, row+1, column)
					else:
						return False
			if (row-1) > 7 or (column) > 7 or (row-1) < 0 or (column) < 0:
					return False
			else:
				if board[row-1][column] == 'W':
					if (row-1) > 7 or (column) > 7 or (row-1) < 0 or (column) < 0:
						return False
					elif board[row-(2)][column] == 'B':
						return True
					elif board[row-(2)][column] == 'W':
						return validMove_vert(board, player, row-1, column)
					else:
						return False
	else: 
		if (row+1) > 7 or (column) > 7 or (row+1) < 0 or (column) < 0:
				return False
		else:
			if board[(row+1)][(column)] == 'B':
				if (row+1) > 7 or (column) > 7 or (row+1) < 0 or (column) < 0:
					return False
				elif board[row+2][column] == 'W':
					return True
				elif board[row+2][column] == 'B':
					return validMove_vert(board, player, row+1, column)
				else:
					return False
		if (row-1) > 7 or (column) > 7 or (row-1) < 0 or (column) < 0:
				return False
		else:
			if board[(row-1)][(column)] == 'B':
				if (row-1) > 7 or (column) > 7 or (row-1) < 0 or (column) < 0:
					return False
				elif board[row-2][column] == 'W':
					return True
				elif board[row-2][column] == 'B':
					return validMove_vert(board, player, row-1, column)
				else:
					return False

'''

'''
			if board[row+1][column-1] == 'W':
				if board[row+2][column-2] == 'B':
					return True
				elif board[row+2][column-2] == 'W':
					return validMove(board, player, row+1, column-1)		
			elif board[row][column-1] == 'W':
				if board[row][column-2] == 'B':
					return True
				elif board[row][column-2] == 'W':
					return validMove(board, player, row, column-1)
			elif board[row-1][column-1] == 'W':
				if board[row-2][column-2] == 'B':
					return True
				elif board[row-2][column-2] == 'W':
					return validMove(board, player, row-1, column-1)
			elif board[row-1][column] == 'W':
				if board[row-2][column] == 'B':
					return True
				elif board[row-2][column] == 'W':
					return validMove(board, player, row-1, column)
			elif board[row-1][column+1] == 'W':
				if board[row-2][column+2] == 'B':
					return True
				elif board[row-2][column+2] == 'W':
					return validMove(board, player, row-1, column+1)
			elif board[row][column+1] == 'W':
				if board[row][column+2] == 'B':
					return True
				elif board[row][column+2] == 'W':
					return validMove(board, player, row, column+1)
			elif board[row+1][column+1] == 'W':
				if board[row+2][column+2] == 'B':
					return True
				elif board[row+2][column+2] == 'W':
					return validMove(board, player, row+1, column+1)
			elif board[row+1][column] == 'W':
				if board[row+2][column] == 'B':
					return True
				elif board[row+2][column] == 'W':
					return validMove(board, player, row+1, column)
			else:
				return False
		else:
			return False
	else:
			if board[row][column] == 0: 
				if board[row+1][column-1] == 'B':
					if board[row+2][column-2] == 'W':
						return True
					elif board[row+2][column-2] == 'B':
						return validMove(board, player, row+1, column-1)
				elif board[row][column-1] == 'B':
					if board[row][column-2] == 'W':
						return True
					elif board[row][column-2] == 'B':
						return validMove(board, player, row, column-1)
				elif board[row-1][column-1] == 'B':
					if board[row-2][column-2] == 'W':
						return True
					elif board[row-2][column-2] == 'B':
						return validMove(board, player, row-1, column-1)
				elif board[row-1][column] == 'B':
					if board[row-2][column] == 'W':
						return True
					elif board[row-2][column] == 'B':
						return validMove(board, player, row-1, column)
				elif board[row-1][column+1] == 'B':
					if board[row-2][column+2] == 'W':
						return True
					elif board[row-2][column+2] == 'B':
						return validMove(board, player, row-1, column+1)
				elif board[row][column+1] == 'B':
					if board[row][column+2] == 'W':
						return True
					elif board[row][column+2] == 'B':
						return validMove(board, player, row, column+1)
				elif board[row+1][column+1] == 'B':
					if board[row+2][column+2] == 'W':
						return True
					elif board[row+2][column+2] == 'B':
						return validMove(board, player, row+1, column+1)
				elif board[row+1][column] == 'B':
					if board[row+2][column] == 'W':
						return True
					elif board[row+2][column] == 'B':
						return validMove(board, player, row+1, column)
				else:
					return False
			else:
				return False

'''

					
def allMoves(board, player):
	lst = []
	for row in range(8):
		for column in range(8):
			if validMove(board,player, row, column):
				lst += [[row, column]]
	return lst



def nextBoard(board, player, move):
	list1=[]
	for a in [1, 0, -1]:
		for b in [1, 0, -1]:
			if a == 0 and b == 0:
				pass 
			list2 = []
			list1 += nextBoard_direct(board, player, move[0], move[1], a, b, list1, list2)
	[updateBoard(board, player, a[0], a[1]) for a in list1]


def nextBoard_direct(board, player, row, column, a, b, lst, new_lst): 
	if player == 1:
		if (row+a) > 7 or (column+b) > 7 or (row+a) < 0 or (column+b) < 0:
			pass
		else:
			if board[row+a][column+b] == 'W':
				new_lst.append([(row+a),(column+b)])
				if (row+(2*a)) > 7 or (column+(2*b)) > 7 or (row+(2*a)) < 0 or (column+(2*b)) < 0:
					pass
				elif board[row+(2*a)][column+(2*b)] == 'B':
					lst += new_lst
				elif board[row+(2*a)][column+(2*b)] == 'W':
					return nextBoard_direct(board, player, row+a, column+b, a, b, lst, new_lst)
				else:
					pass
		return lst
	else: 
		if (row+a) > 7 or (column+b) > 7 or (row+a) < 0 or (column+b) < 0:
			pass
		else:	
			if board[(row+a)][(column+b)] == 'B':
				new_lst.append([(row+a),(column+b)])
				if (row+(2*a)) > 7 or (column+(2*b)) > 7 or (row+(2*a)) < 0 or (column+(2*b)) < 0:
					pass
				elif board[row+(2*a)][column+(2*b)] == 'W':
					lst += new_lst
				elif board[row+(2*a)][column+(2*b)] == 'B':
					return nextBoard_direct(board, player, row+a, column+b, a, b, lst, new_lst)
				else:
					pass
		return lst


def updateScreen(board):
	for i in range(8):
		for a in range(8):
			if board[i][a] =='B':
				stampPlayer(i,a,1)
			if board[i][a] =='W':
				stampPlayer(i,a,2)

'''
def nextboard_vert(board, player, row, column, lst):
	lst = []
	if player == 1:
			if (row+1) > 7 or (column) > 7 or (row+1) < 0 or (column) < 0:
					pass
			else:
				if board[row+1][column] == 'W':
					new_lst=[]
					if (row+1) > 7 or (column) > 7 or (row+1) < 0 or (column) < 0:
						pass
					elif board[row+(2)][column] == 'B':
						lst.append(new_lst)
					elif board[row+(2)][column] == 'W':
						new_lst.append([(row+1),column])
						return nextboard_vert(board, player, row+1, column, new_lst)
					else:
						pass
			if (row-1) > 7 or (column) > 7 or (row-1) < 0 or (column) < 0:
					return False
			else:
				if board[row-1][column] == 'W':
					new_lst=[]
					if (row-1) > 7 or (column) > 7 or (row-1) < 0 or (column) < 0:
						pass
					elif board[row-(2)][column] == 'B':
						lst.append(new_lst)
					elif board[row-(2)][column] == 'W':
						new_lst.append([(row-1),column])
						return nextboard_vert(board, player, row-1, column, new_lst)
					else:
						pass
	else: 
		if (row+1) > 7 or (column) > 7 or (row+1) < 0 or (column) < 0:
				return False
		else:
			if board[(row+1)][(column)] == 'B':
				if (row+1) > 7 or (column) > 7 or (row+1) < 0 or (column) < 0:
					return False
				elif board[row+2][column] == 'W':
					lst.append([(row+1),column])
					return True
				elif board[row+2][column] == 'B':
					lst.append([(row+1),column])
					return nextboard_direct(board, player, row+1, column, new_lst)
				else:
					return False
		if (row-1) > 7 or (column) > 7 or (row-1) < 0 or (column) < 0:
				return False
		else:
			if board[(row-1)][(column)] == 'B':
				if (row-1) > 7 or (column) > 7 or (row-1) < 0 or (column) < 0:
					return False
				elif board[row-2][column] == 'W':
					return True
				elif board[row-2][column] == 'B':
					return nextboard_direct(board, player, row-1, column, new_lst)
				else:
					return False
	return lst
'''
'''
def game(xcoord, ycoord):
	global turn
	player = turn % 2
	if player == 0:
		player = 2
	if len(allMoves(gameboard,1)) + len(allMoves(gameboard,2))==0:
		t.goto(-50,275)
		t.pendown()
		t.write('Game Over')
		t.penup()
	row = whichRow(ycoord)
	column = whichColumn(xcoord)
	if [row, column ] in allMoves(gameboard, player):
		stampPlayer(row, column, player)
		updateBoard(gameboard, player, row, column)
		nextBoard(gameboard, player, [row, column])
		updateScreen(gameboard)
		updateScore(gameboard)
		turn += 1
		
initialize()
s.onclick(game)
s.mainloop()

'''

import copy

def nextBoard2(board, player, move):
	jboard = copy.deepcopy(board)
	list1=[]
	for a in [1, 0, -1]:
		for b in [1, 0, -1]:
			if a == 0 and b == 0:
				pass 
			list2 = []
			list1 += nextBoard_direct(jboard, player, move[0], move[1], a, b, list1, list2)
	[updateBoard(jboard, player, a[0], a[1]) for a in list1]
	updateBoard(jboard, player, move[0], move[1])
	return jboard



def evaluate(board, player):
	score = 0
	if player == 1:
		score = (calculateScore(board, 1)-calculateScore(board,2))
		score += (len(allMoves(board, 1))*10)
		if board[0][0]=='B' or board[0][7]=='B' or board[7][0] == 'B' or board[7][7] == 'B':
			score += 100
		if board[0][0]=='W' or board[0][7]=='W' or board[7][0] == 'W' or board[7][7] == 'W':
			score -= 50
		if len(allMoves(board,2))==0:
			score += 1000
	else:
		score = (calculateScore(board, 2)-calculateScore(board,1))
		score += (len(allMoves(board, 2))*10)
		if board[0][0]=='W' or board[0][7]=='W' or board[7][0] == 'W' or board[7][7] == 'W':
			score += 100
		if board[0][0]=='B' or board[0][7]=='B' or board[7][0] == 'B' or board[7][7] == 'B':
			score -= 50
		if len(allMoves(board,1))==0:
			score += 1000
	return score



def minimax(board, depth, max_depth, a, b, max_player, min_player):
	global move
	fake_board = copy.deepcopy(board)
	if depth%2 == 0:
		moves_list = allMoves(fake_board,max_player)
		boards_list = [[nextBoard2(fake_board, max_player, a),a] for a in moves_list]
	else:
		moves_list = allMoves(fake_board, min_player)
		boards_list = [[nextBoard2(fake_board, min_player, a),a] for a in moves_list]
	#print (moves_list)
	if depth == max_depth or len(boards_list) == 0:
		#print (evaluate(board, max_player))
		return evaluate(board, max_player)
	else:
		if depth%2 == 0:
			maxEval = float('-inf')
			for n in boards_list:
				#print (n[1])
				h = minimax(n[0], depth+1, max_depth, a, b, max_player, min_player)
				maxEval = max(maxEval,h)
				a = max(a,h)
				if h == min(a,h):
					move = n[1]
				if b <= a:
					break
			if depth == 0:
				return move
			return maxEval
		if depth%2 == 1:
			minEval = float('inf')
			for i in boards_list:
				#print (i[1])
				h = minimax(i[0], depth+1, max_depth, a, b, max_player, min_player)
				minEval = min(minEval,h)
				b = min(b,h)
				if h == min(b,h):
					move = i[1]
				if b <= a:
					break
			if depth == 0:
				return move
			return minEval

def bot_nathan(board, player, depth):
	move =[]
	if player ==1:
		maxi_player = 1
		mini_player =2
	else:
		maxi_player = 2
		mini_player =1
	best_move = minimax(board, 0, depth, float('-inf'), float('inf'), maxi_player, mini_player)
	print ('best move' + str(best_move))
	nextBoard(board, player, best_move)
	updateBoard(board, player, best_move[0],best_move[1])
	updateScreen(board)

def play(board, player, move):
	nextBoard(board, player, move)
	updateBoard(board, player, move[0],move[1])
	updateScreen(board)


'''
if depth%2 == 0:
			a = evaluate(board)
		else:
			b = evaluate(board)
'''
'''

def Alpha_Beta_Search(state):
	v = max(state,float('-inf'), float('inf'))
	return v

def Max_Value(state, a, b):
	return

'''

def Translate(board):
	for i in range(8):
		for a in range(8):
			if board[i][a] == 'b'
				board[i][a] = 'B'
			elif board[i][a] == 'w'
				board[i][a] = 'W'
			else:
				board[i][a] = 0
	return board
