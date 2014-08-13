def WinnerQ(pos):
	if (pos[0]=='x' and pos[1] == 'x' and pos[2] == 'x') or (pos[3]=='x' and pos[4] == 'x' and pos[5] == 'x') or (pos[6]=='x' and pos[7] == 'x' and pos[8] == 'x') or (pos[0]=='x' and pos[3] == 'x' and pos[6] == 'x') or (pos[1]=='x' and pos[4] == 'x' and pos[7] == 'x') or (pos[2]=='x' and pos[5] == 'x' and pos[8] == 'x') or (pos[0]=='x' and pos[4] == 'x' and pos[8] == 'x') or (pos[2]=='x' and pos[4] == 'x' and pos[6] == 'x'):
		return 'x'
	elif (pos[0]=='o' and pos[1] == 'o' and pos[2] == 'o') or (pos[3]=='o' and pos[4] == 'o' and pos[5] == 'o') or (pos[6]=='o' and pos[7] == 'o' and pos[8] == 'o') or (pos[0]=='o' and pos[3] == 'o' and pos[6] == 'o') or (pos[1]=='o' and pos[4] == 'o' and pos[7] == 'o') or (pos[2]=='o' and pos[5] == 'o' and pos[8] == 'o') or (pos[0]=='o' and pos[4] == 'o' and pos[8] == 'o') or (pos[2]=='o' and pos[4] == 'o' and pos[6] == 'o'):
		return 'o'
	else:
		return 'n'

def evenGameQ(pos):
	check = 0
	for i in range(9):
		if pos[i] == 'n':
			pos_copy = pos[:]
			pos_copy[i] = 'x'
			if WinnerQ(pos_copy) == 'x':
				check = 1
				break
	for i in range(9):
		if pos[i] == 'n':
			pos_copy = pos[:]
			pos_copy[i] = 'o'
			if WinnerQ(pos_copy) == 'o':
				check = 2
				break
	if check == 2:
		return True
	else:
		return False

def winningSquareQ(pos):
	for i in range(9):
		if pos[i] == 'n':
			pos_copy = pos[:]
			pos_copy[i] = 'o'
			if WinnerQ(pos_copy) == 'o':
				return i
	return -1

def gameOverQ(pos):
	for sq in pos:
		if sq == 'n':
			return False
	return True

def tieGameQ(pos):
	pos_copy = pos[:]
	for i in range(9):
		if pos_copy[i] == 'n':
			pos_copy[i] = 'x'
	if WinnerQ(pos_copy) == 'x':
		return False
	pos_copy2 = pos[:]
	for i in range(9):
		if pos_copy[i] == 'n':
			pos_copy[i] = 'o'
	if WinnerQ(pos_copy) == 'o':
		return False
	return True