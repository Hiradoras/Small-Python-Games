import time, sys, shutil

s = 0.02
while True:
	print("Welcome. I have 3 patterns for now. type 1 or 2 or 3 select")
	pattern = input(": ")


	if pattern == "1":
		try:
			while True:
				for i in range(5,-1,-1):
					print(' '*i + '*****')
					time.sleep(s)
					if i == 0:
						for z in range(1,6):
							print(' '*z + "*****")
							time.sleep(s)

		except KeyboardInterrupt:
			print("bye!")
			continue

	elif pattern == "2":
		try:
			while True:
				for i in range(5,-1,-1):
					print(' '*i + '*'+' '*i + '*'+' '*i + '**')
					time.sleep(s)
					if i == 0:
						for z in range(1,6):
							print(' '*z + "*"+' '*z + "*"+' '*z + "**")
							time.sleep(s)

		except KeyboardInterrupt:	
			print("bye!")
			continue


	elif pattern == "3":

		WIDTH = shutil.get_terminal_size()[0]
		WIDTH -=3
		try:
			while True:
				for i in range(0,WIDTH//2):
					print(" "*i + "* *" + "  "*(WIDTH-i) + "* *")
					time.sleep(s)
					if i == (WIDTH//2)-1:
						for z in range(WIDTH//2,-1,-1):
							print(" "*z + "***" + "  "*(WIDTH-z) + "***")
							time.sleep(s)
					

		except KeyboardInterrupt:
			print("bye!")
			continue



