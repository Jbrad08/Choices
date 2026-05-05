#dependencies

import time
import console


#Settings
Name = "Choices"
author = "Jon Bradley"
startupmode = True
gameloop = True
customgames = True
tutorial = True

#defines

global customgamecreated, cmain, caans, cbans, ccans, csm, cim
customgamecreated = False

cmain = ""
caans = ""
cbans = ""
ccans = ""
csm = ""
cim = ""

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
    
def clear():
 	console.clear()
#startup

def startup():
	for i in range(6):
		print("Starting")
		time.sleep(0.5)
		clear()
		print("Starting.")
		time.sleep(0.5)
		clear()
		print("Starting..")
		time.sleep(0.5)
		clear()
		print("Starting...")
		time.sleep(0.5)
		clear()
	print("Starting...")
	time.sleep(1)
	clear()
	time.sleep(1)
	print("WELCOME")
	time.sleep(1)
	print("A game made by",author)
	time.sleep(2)
	clear()
	time.sleep(5)


def begin():
	print(Name)
	print("Press enter to start!")
	input()
	clear()
	
	if tutorial:
		slow_print(f"welcome to {Name }")
		time.sleep(0.5)
		slow_print("First of all")
		time.sleep(0.5)
		slow_print("we will do the tutorial.")
		time.sleep(2)
		clear()
		time.sleep(1)
		slow_print("This game will give you different scenearios.")
		time.sleep(1)
		slow_print("You will either choose to do option a or b.")
		time.sleep(1)
		slow_print("Each option you make will decide your fate in the end.")
		time.sleep(1)
		slow_print("Make wise choices")
		time.sleep(3)
		print("If you would like to do a tutorial game type y, if not type n")
		while True:
			tr = input("Y/N: ").strip().lower()
			if tr == "y":
				tut()
				break
			elif tr == "n":
				notut()
				break
			else:
				print("only Y/N")
		
def tut():
	clear()
	print("Wise choose.")
	time.sleep(1)
	clear()
	time.sleep(3)
	print("Tutorial")
	print(" ")
	time.sleep(1)
	slow_print("You are tapped in a jungle and need to escape!")
	slow_print(" Quick!! you have 2 options to try to escape.")
	print("")
	time.sleep(2)
	slow_print("You notice a remote tribe. You could try to talk to thelm and hope they can help get rescue, but at worst they could be dangrous and KILL you.")
	print("")
	slow_print("You could also find sticks and spell SOS in the sand. At best a plane flying overhead could see your sign and rescue you. At worst you DIE of hunger while waiting.")
	print("")
	time.sleep(2)
	print("A - You contact the tribe.")
	print("B - You make the SOS sign")
	time.sleep(1)
	while True:
		tans = input("a or b").strip().lower()
		clear()
		if tans == "a":
			time.sleep(1)
			print("You")
			time.sleep(0.5)
			clear()
			slow_print("You D")
			time.sleep(0.5)
			clear()
			print("You Survive!!")
			time.sleep(0.3)
			slow_print("The tribe had a GPS phone and was able to call for help. You are airlifted later that day.")
			time.sleep(5)
			break
			
		elif tans == "b":
			time.sleep(1)
			slow_print("You Died.")
			time.sleep(0.3)
			slow_print("You die of exhaustion and starvation. You where already staving and pushed yourselve over the limit after making the SOS sign.")
			time.sleep(8)
			break
		else:
			print("only A/B")
		
		time.sleep(1)
		slow_print("Press enter to continue")
		input().strip().lower()
		clear()
		menu()


def notut():
	clear()
	print("I guess you Have Played These Games Before")
	time.sleep(3)
	menu()
		
		
def menu():
	global customgamecreated
	level = 67
	clear()
	print(Name)
	print("1 - New Game")
	print("")
	print("2 - Continue on Level",level)
	print("")
	if customgames:
		print("3 - Custom")
	if customgamecreated and customgames:
		print("")
		print("4 - Play Previous Custom Game")
	
	menuans = int(input())
    
	if menuans == 1:
		print("new game")
	if menuans == 2:
	 	print("resume game")
	if customgames:
		if menuans == 3:
	 		custommaker()
	if customgamecreated and customgames:
		if menuans == 4:
			customrun()
			




def custommaker():
	clear()
	global customgamecreated, cmain, caans, cbans, ccans, csm, cim
	customgamecreated = False
	print("")
	print("")
	print("")
	print("")
	print("3 - Make custom")
	time.sleep(1)
	clear()
	slow_print("I see you have chosen to make a custom game.")
	time.sleep(0.5)
	clear()
	print("Custom Game Maker")
	print("")
	print("")
	slow_print("What would you like your main question to be?")
	cmain = input("any string").strip()
	time.sleep(2)
	clear()
	print("Custom Game Maker")
	print("")
	print("")
	slow_print("What would you like option a to be?")
	caans = input("any string").strip()
	clear()
	print("Custom Game Maker")
	print("")
	print("")
	slow_print("What would you like option b to be?")
	cbans = input("any string").strip()
	clear()
	print("Custom Game Maker")
	print("")
	print("")
	slow_print("Which option is correct?")
	while True:
		ccans = input("a or b").strip().lower()
		if ccans == "a":
			break
		elif ccans == "b":
			break
		else:
			print("only A/B")
	
	clear()
	print("Custom Game Maker")
	print("")
	print("")
	slow_print("Custom correct message")
	csm = input("any string").strip()
	clear()
	print("Custom Game Maker")
	print("")
	print("")
	slow_print("Custom incorrect message")
	cim = input("any string").strip()
	clear()
	time.sleep(5)
	customgamecreated = True
	print("Would you like to run the game now")
	time.sleep(1)
	while True:
		cgmf = input("Y/N: ").strip().lower()
		if cgmf == "y":
			customrun()
			break
		elif cgmf == "n":
			menu()
			break
		else:
			print("only Y/N")
		
def customrun():
	global cmain, caans, cbans, ccans, csm, cim
	clear()
	print("loading custom game")
	time.sleep(2)
	clear()

	print("Custom Game\n")
	time.sleep(1)

	slow_print(f"{cmain}")
	print()
	time.sleep(1)

	slow_print(f"a - {caans}")
	slow_print(f"b - {cbans}")
	while True:
		cans = input("a or b: ").strip().lower()
		if cans == ccans:
			slow_print(f"{csm}")
			clear()
			break
		elif cans != ccans:
			slow_print(f"{cim}")
			clear()
			break
		else:
			print("only A/B")

		if cans == ccans:
			time.sleep(1)
			slow_print(f"{csm}")
		else:
			time.sleep(1)
			slow_print(f"{cim}")
		time.sleep(5)
		clear()
		menu()
	
	
	
	
	
	
	
	
def main():
	begin()
	menu()
	
	
#main game script
if startupmode:
    startup()

if gameloop:
    while True:
        main()
else:
    main()
    
    

	
	
