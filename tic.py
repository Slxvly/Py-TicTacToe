import os

class Game:
	def __init__(self, players):
		self.players = players
		self.board = [-1] * 9
		
	def nextRound(self, player):
		self.paint()
		br(1)
		choice = input("Gib die Zahl eines Feldes an: \n> ")
		
		while True:
			try:
				number = int(choice)
				if number > 9 or number < 1:
					raise ValueException("Out of bounds.")
				if self.board[number - 1] != -1:
					raise ValueException("Already set.")
				self.board[number - 1] = 0 if player == 0 else 1
				break
			except:
				choice = input("Versuche es erneut: \n> ")
	
	def paint(self):
		cls()
		array = [""] * 9
		for i in range(len(self.board)): 
			element = self.board[i]
			array[i] = "X" if element == 0 else ("O" if element == 1 else i + 1)
		print(array[0], array[1], array[2])
		print(array[3], array[4], array[5])
		print(array[6], array[7], array[8])
		
	def check(self):
		b = self.board
		if b[0] == b[1] == b[2]:
			return b[0]
		if b[3] == b[4] == b[5]:
			return b[3]
		if b[6] == b[7] == b[8]:
			return b[6]
		if b[0] == b[3] == b[6]:
			return b[0]
		if b[1] == b[4] == b[7]:
			return b[1]
		if b[2] == b[5] == b[8]:
			return b[2]
		if b[0] == b[4] == b[8]:
			return b[0]
		if b[2] == b[4] == b[6]:
			return b[2]
		return -1

def br(amount):
	print("\n" * amount)

def cls():
	os.system("cls" if os.name=="nt" else "clear")

p1 = input("Name des 1. Spielers: \n> ")
p2 = input("Name des 2. Spielers: \n> ")

game = Game([p1, p2])

p = 1
for i in range(9):
	p = 1 if p == 0 else 0
	game.nextRound(p)
	if game.check() != -1:
		game.paint()
		br(1)
		print(game.players[p], "hat das Spiel gewonnen.")
		break
if game.check() == -1:
	print("Das Spiel wurde unentschieden gespielt.")