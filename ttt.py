
startStrategy = [	
					0.0202249, 0.0201317, 0.0200378, 0.0199485, 0.0198641, 0.0197838,
					0.0197072, 0.0196346, 0.0195659, 0.019501, 0.0194391, 0.0193796,
					0.0193228, 0.019269, 0.0192189, 0.0191733, 0.0191312, 0.019092,
					0.0190567, 0.0190265, 0.0190019, 0.0189824, 0.0189672, 0.0189565,
					0.0189507, 0.01895, 0.0189544, 0.0189646, 0.0189795, 0.0190004,
					0.0190268, 0.0190586, 0.0190943, 0.0191331, 0.0191762, 0.0192237, 
					0.0192755, 0.0193307, 0.0193887, 0.0194489, 0.0195126, 0.0195799,
					0.0196509, 0.019726, 0.0198045, 0.0198867, 0.0199737, 0.0200657,
					0.0201612, 0.0202488, 0.0201593, 0.00885816
				]

def getStrategy(pos, p1, p2):
	num = posToNumber(pos)
	if num == 0:
		return startStrategy
	reducednum = reduceNum(num)
	pos_file = open('Database/'+str(reducednum)+'.csv','r').read().split('\n')
	line = pos_file[p1-1].split(',')
	strat = []
	for i in range(1, len(line)):
		strat.append(float(line[i]))
	return strat

def getMove(pos, p1, p2):
	positions = []
	for i in range(0,9):
		if pos[i] != 'n':
			positions.append(-1)
			continue
		next_pos = pos[:]
		next_pos[i] = 'o'
		num = posToNumber(next_pos)
		reducednum = reduceNum(num)
		pos_file = open('Database/'+str(reducednum)+'.csv','r').read().split('\n')
		line = pos_file[p1].split(',')
		positions.append(float(line[0]))
	return positions.index(max(positions))

def reduceNum(num):
	return int(open('Database/vertices.csv','r').read().split('\n')[num])

def posToNumber(pos):
	conv = {'n':0,'o':1,'x':2}
	s = 0
	for i in range(0,9):
		s += conv[pos[8-i]]*3**i
	return s

def squaresRemainingQ(pos):
	num = 0
	for s in pos:
		if s == 'n':
			num += 1
	return num

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
				check += 1
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