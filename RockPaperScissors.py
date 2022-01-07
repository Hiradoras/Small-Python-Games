import random, sys, time


wins, losses, ties = 0, 0, 0

while True:
	time.sleep(0.5)
	print("%s Wins, %s Losses, %s Ties" %(wins, losses, ties))	
	while True:
		time.sleep(0.5)
		print("Enter your move! 'R' for Rock, 'P' for Paper and 'S' for Scissor ('q' for exit): ")
		player = input().lower()
		if player == "q":
			print("Good Bye!")
			sys.exit()
		if player == "r" or player == "p" or player == "s":
			break
		print("Please tpye r or p or s or q only!")

	if player == "r":
		print("Rock versus...")
	elif player == "p":
		print("Paper versus...")
	elif player == "s":
		print("Scissor versus...")
	time.sleep(0.5)
	randomNumber = random.randint(1,3)
	if randomNumber == 1:
		computer = "r"
		print("Rock")
	elif randomNumber == 2:
		computer = "p"
		print("Paper")
	elif randomNumber == 3:
		computer = "s"
		print("Scissor")

	time.sleep(0.3)
	if player==computer:
		ties+=1
		print("Tie!")

	#Wins
	elif player=="r" and computer=="s":
		print("You won!")
		wins+=1
	elif player=="s" and computer=="p":
		print("You won!")
		wins+=1
	elif player=="p" and computer=="r":
		print("You won!")
		wins+=1

	#Loses
	elif player=="r" and computer=="p":
		print("You lose!")
		losses+=1
	elif player=="p" and computer=="s":
		print("You lose!")
		losses+=1
	elif player== "s" and computer=="r":
		print("You lose")
		losses+=1




