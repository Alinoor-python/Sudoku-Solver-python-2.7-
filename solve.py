
def check_value(board,num,row,col):
	horizontal=board[row]
	horizontal[col]=0
	vertical=[]
	for i in range(9):
		vertical.append(board[i][col])
	vertical[row]=0
	box=[]
	box_x,box_y=0,0
	for i in range(0,9,3):
		if (col)-i<3:
			box_x=i
			break
	for i in range(0,9,3):
		if (row)-i<3:
			box_y=i
			break
	for i in range(3):
		box.append(board[box_y][box_x+i])
		box.append(board[box_y+1][box_x+i])
		box.append(board[box_y+2][box_x+i])
	if num in horizontal or num in vertical or num in box:
		return False
	else:
		return True
def find(board):
	for i in range(9):
		for j in range(9):
			if board[i][j]==0:
				return i,j
			if i==8 and j==8:
				return None
def solve(board):
	
	if not find(board):
		return True
	
	else:
		row,col=find(board)
		for i in range(1,10):
			if check_value(board,i,row,col):
				board[row][col]=i
				
				if solve(board):
					return True
				board[row][col]=0
		return False