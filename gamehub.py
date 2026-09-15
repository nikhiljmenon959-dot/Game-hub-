import random
from datetime import datetime, timedelta
import poppu
print("welcome to game hub!")
#wack a mole
def wackmole():	
    print("Welcome to Whack-a-Mole!")
    tb = datetime.now()
    ta = tb + timedelta(minutes=1)
    grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    mole = "=o="
    score = 0
    print("Game ends at:", ta.strftime("%H:%M:%S"))
    
    while True:
        tb = datetime.now()
        if tb >= ta:
            print("\n--- GAME OVER ---")
            print(f"Final Score: {score}")
            break
        mole_index = random.randint(0, 8)
        original_value = grid[mole_index] 
        grid[mole_index] = mole
        print("\n" + str(grid[0:3]))
        print(str(grid[3:6]))
        print(str(grid[6:9]))
        choice = input("Enter the square u want to hit (1-9): ").strip()
        if choice == original_value:
            print("💥 HIT!")
            score += 1
        else:
            print("❌ MISS!")
        grid[mole_index] = original_value
        print(f"Current Score: {score}")

		
			

def rps():
	print("welcome to rock paper scissor")
	computer=0
	player=0
	l = ["rock", "paper", "scissor"]
	while computer < 5 and player < 5:
	       coch = random.choice(l)
	       uch = input("enter your choice ")
	       if coch == "rock" and uch == "paper":
	       	player = player + 1
	       elif coch == "paper" and uch == "rock":
	       	computer = computer + 1
	       elif coch == "paper" and uch == "scissor":
	       	player = player + 1
	       elif coch == "scissor" and uch == "paper":
	       	computer = computer + 1
	       elif coch == "scissor" and uch == "rock":
	       	player = player + 1
	       elif coch == "rock" and uch == "scissor":
	       	computer = computer + 1
	       elif coch==uch:
	       	print("its a tie")
	       else:
	       	print("wrong input try again ")
	       print("score of computer", computer, "score of player=", player)
	if player == 5:
	   print("player wins")
	elif computer == 5:
		print("computer wins")
		
#tic tac tow
def ttt():
    print("Welcome to Tic-Tac-Toe!")
    
    Tutorial = """Tic-tac-toe is a two-player game.
Players take turns placing X or O on a 3x3 board.
The first player to get three in a row wins."""
    
    print(Tutorial)
    input("\nPress Enter to start")

    print("\nMULTIPLAYER")
    
    player1 = input("Player 1 enter your name: ")
    
    while True:
        player2 = input("Player 2 enter your name: ")
        
        if player1 == player2:
            print("Name already exists. Choose another name.")
        else:
            break

    # Player 1 chooses X or O
    while True:
        mark = input(player1 + ", choose your notation (x/o): ").lower()

        if mark == "x":
            pl1 = "X"
            pl2 = "O"
            break

        elif mark == "o":
            pl1 = "O"
            pl2 = "X"
            break

        else:
            print("Invalid notation. Please try again.")

    print(player1, "=", pl1)
    print(player2, "=", pl2)

    # The board
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    # Winning combinations
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    turn = 0

    while turn < 9:

        # Display board
        print()
        print(board[0], "|", board[1], "|", board[2])
        print("--+---+--")
        print(board[3], "|", board[4], "|", board[5])
        print("--+---+--")
        print(board[6], "|", board[7], "|", board[8])
        print()

        # Decide whose turn
        if turn % 2 == 0:
            player = player1
            symbol = pl1
        else:
            player = player2
            symbol = pl2

        print(player, "it's your turn")

        position = input("Enter position from 1 to 9: ")

        # Check valid position
        if position not in board:
            print("Position already occupied or invalid. Try again.")
            continue

        # Place symbol
        index = board.index(position)
        board[index] = symbol

        turn = turn + 1

        # Check winning combinations
        winner = False

        for a, b, c in wins:
            if board[a] == board[b] == board[c] == symbol:
                winner = True
                break

        if winner:
            print()
            print(board[0], "|", board[1], "|", board[2])
            print("--+---+--")
            print(board[3], "|", board[4], "|", board[5])
            print("--+---+--")
            print(board[6], "|", board[7], "|", board[8])
            
            print()
            print(player, "wins!")
            break

    else:
        print()
        print(board[0], "|", board[1], "|", board[2])
        print("--+---+--")
        print(board[3], "|", board[4], "|", board[5])
        print("--+---+--")
        print(board[6], "|", board[7], "|", board[8])
        
        print("\nIt's a draw!")

    print("\nTHANK YOU FOR PLAYING")

#odd or even
def oddeven():
	def c():
		l=[0,1,2,3,4,5,6]
		cch=random.choice(l)
		return cch
	def p():
			while True:
				plin=input("enter the number from 0 to 6:")
				if plin in ["0","1","3","2","4","5","6"]:
					break
				else:
					print("wrong input try again")
			return plin
			
	print("wellcome to odd or even hand cricket")
	print("rules The Toss: Players decide who is Odd or Even and simultaneously show a number of fingers. If the sum of the fingers shown is odd or even, the winner chooses to bat or bowl.The Goal: The batter tries to score as many runs as possible, while the bowler tries to get the batter out.")
	player=input("enter your name:")
	while True:
		pc=input("enter your choice for the toss odd or even:")
		if pc=="odd":
			print("player chose odd")
			print("computer chose even")
			break
		elif pc=="even":
			print("player chose even")
			print("computer chose even")
			break
		else:
			print("invalid choice try again")
	toss=c()
	pin=p()						
	tosto=toss+int(pin)
	print("the toss:",tosto)
	if pc=="odd":
		if tosto%2!=0:
			tossw=1
			print("player wins the toss")
		else:
			tossw=0
			print("computer wins the toss")
	elif pc=="even":
		if tosto%2==0:
			tossw=1
			print("player wins the toss")
		else:
			tossw=0
			print("computer wins the toss")
	if tossw==1:
		while True:
			borb=input("enter would you like to bat or ball:")
			if borb=="bat":
				pl="bat"
				co="ball"
				print("player chose bating")
				print("computer chose balling")
				break
			elif borb=="ball":
				pl="ball"
				co="bat"
				print("player chose balling")
				print("computer chose bating")
				break
	elif tossw==0:
		chb=random.choice(["bat","ball"])
		if chb=="bat":
			co="bat"
			pl="ball"
			print("computer has chosen bating")
			print("player balling")
		elif chb=="ball":
			co="ball"
			pl="bat"
			print("computer has chosen balling")
			print("player bating")		
	playerscore=0
	computerscore=0
	for i in range(0,2,1):
		if i==0:
			while True:
				if pl=="bat"or co=="ball":
					roll=c()
					proll=p()
					if roll==int(proll):
						print("playet is out ")
						print("player score",playerscore)
						break
					else:
						playerscore=playerscore+int(proll)
				elif pl=="ball"or co=="bat":
						roll=c()
						proll=p()
						if roll==int(proll):
							print("computer is out ")
							print("computer score",computerscore)
							break
						else:
							computerscore=computerscore+roll
		elif i==1:
			temp=pl
			pl=co
			co=temp
			while True:
				if pl=="bat"or co=="ball":
					roll=c()
					proll=p()
					if roll==int(proll):
						print("playet is out ")
						print("player score",playerscore)
						break
					else:
						playerscore=playerscore+int(proll)
				elif pl=="ball"or co=="bat":
						roll=c()
						proll=p()
						if roll==int(proll):
							print("computer is out ")
							print("computer score",computerscore)
							break
						else:
									computerscore=computerscore+roll
	if playerscore>computerscore:
		print(player," wins")
	elif playerscore<computerscore:
		print("computer wins")
	else:
		print("it is a tie")
	
									
	
ui=1
while ui==1:
	print("enter\n1:for rock paper scissor\n2:for tic tac tow multipayer\n3:for odd or even\n4 for poppu the cat simulator\n5:for wack a mole \nenter exit  to exit")
	cho=input("enter your choice ")
	if cho=="1":
		rps()
		print("would you like to play another game?")
	elif cho=="2":
		ttt()
		print("would you like to play another game?")
	elif cho=="3":
		oddeven()
		print("would you like to play another game ?")
	elif cho=="4":
		poppu.main()
	elif cho=="5":
		wackmole()
	elif cho=="exit":
		print("Thank you for playing")
		ui=2
	else:
		print("invalid choice")
