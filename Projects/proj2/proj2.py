# File:    proj2.py
# Author:  Ujjwal Rehani
# Date:    4/13/2017 
# Section: 21
# E-mail:  urehani1@umbc.edu 
# Description:
#  This project simulates a vending machine

SNACK_NAME = 0	#zero index is name
SNACK_PRICE = 1  #first index is price
SNACK_QUANTITY = 2	#second index is quantity
SNACK_CODE = 3	#third index is snack code

# printGreeting() explains the program to the user
# Input:          none
# Output:         none (prints greeting)
def printGreeting():
	print("This program simulates a vending machine.  You")
	print("may choose which vending machine you 'load' in,")
	print("and may also specify how much money you have")
	print("available for purchasing vending machine items.\n")
	
# loadFile() reads in file and creates 3d list
# Input:          none
# Output:  machineList       a 3d list
def loadFile():
	machineList = []
	itemList = []
	fileName = input("Please enter file to load machine from: ")
	myFile = open(fileName,"r")
	count = 0
	
	#Creates lists for each snack
	for line in myFile:
		row = []
		line = line.strip()
		name, price, quantity, code = line.split()
		
		row.append(name)
		row.append(price)
		row.append(quantity)
		row.append(code)
		
		itemList.append(row)
			
	machineList.append(itemList)
	myFile.close()

	return machineList
	
# displayMachine() prints out current vending machine
# Input: itemList    the 3d list that contains all the snacks
# Output:         none (prints items and their info)
def displayMachine(itemList):
	count = 0;
	count2 = 0;
	count3 = 0;
	while(count < len(itemList[0]) ):
		if(itemList[0][count][SNACK_QUANTITY] == 0):
			print(end="")
		else:
			print("\t",itemList[0][count][SNACK_NAME],end="")
		count+=1
	print()
	while(count2 < len(itemList[0]) ):
		if(itemList[0][count2][SNACK_QUANTITY] == 0):
			print(end="")
		else:
			print("\t",itemList[0][count2][SNACK_PRICE],end="")
		count2+=1
	print()
	while(count3 < len(itemList[0]) ):
		if(itemList[0][count3][SNACK_QUANTITY] == 0):
			print(end="")
		else:
			print("\t",itemList[0][count3][SNACK_CODE],end="")
		count3+=1
	print()
	
# displayBalance() prints out balance on card
# Input: initialBalance  the balance that is first loaded on card
# Output: balance;   amount of money on card
def displayBalance(initialBalance):
	print("You have $",initialBalance,"left on your card.")
	
# addMoney() adds money to card
# Input: balance; 		amount of money currently on card
# Output: newBalance; 	balance after adding money
def addMoney(balance):
	print("Please enter the amount of money you want to add to your card.")
	newMoney = float(input("Enter a decimal number (greater than or equal to zero): "))
	
	#Checks for positive amount
	while(newMoney < 0):
		newMoney = float(input("Enter a decimal number (greater than or equal to zero): "))
	
	newBalance = balance + newMoney	
	return newBalance
	

# menuChoice() displays menu and asks user to select an option
# Input:		None
# Output: 		None (prints choices)
def menuChoice(snackList,initialBalance):
	okChoices = ["1","2","3","4","5"]
	userChoice = ""
	print("1 - Display Vending Machine")
	print("2 - Make Selection")
	print("3 - Display Card Balance")
	print("4 - Add Money to Card")
	print("5 - Quit")
	print()
	
	#Programs runs unless quit is chosen
	while(userChoice != "5"):
		userChoice = input("Enter a number between 1 and 5 (inclusive): ")
		#Checks for valid input
		while(userChoice not in okChoices):
			userChoice = input("Enter a number between 1 and 5 (inclusive): ")
			
		#Calls respective function based on choice	
		if (userChoice == "1"):
			displayMachine(snackList)
			
			print()
			print("1 - Display Vending Machine")
			print("2 - Make Selection")
			print("3 - Display Card Balance")
			print("4 - Add Money to Card")
			print("5 - Quit")
			print()
			
		elif (userChoice == "2"):
			newList,newMoney = makeSelection(snackList,initialBalance)
			snackList = newList
			initialBalance = newMoney
			
			print()
			print("1 - Display Vending Machine")
			print("2 - Make Selection")
			print("3 - Display Card Balance")
			print("4 - Add Money to Card")
			print("5 - Quit")
			print()
			
		elif (userChoice == "3"):
			displayBalance(initialBalance)
			
			print()
			print("1 - Display Vending Machine")
			print("2 - Make Selection")
			print("3 - Display Card Balance")
			print("4 - Add Money to Card")
			print("5 - Quit")
			print()
			
		elif (userChoice == "4"):
			initialBalance = addMoney(initialBalance)
			print("1 - Display Vending Machine")
			print("2 - Make Selection")
			print("3 - Display Card Balance")
			print("4 - Add Money to Card")
			print("5 - Quit")
			print()
			
		elif (userChoice == "5"):
			saveFile(snackList)
		

# firstBalance() asks user for the initial amount to be put on card
# Input: 	None
# Output: first_balance 	the initial amount of money on card
def firstBalance():
	print("Please enter the amount of money you have on your card.")
	first_balance = float(input("Enter a decimal number (greater than or equal to zero): "))
	
	#Checks for positive balance
	while (first_balance < 0):
		print("The decimal number must be positive.  Please try again!")
		first_balance = float(input("Enter a decimal number (greater than or equal to zero): "))
	
	return first_balance
	
# makeSelection() makes the selection for user and updates list and money
# Input: itemList, money   list with all the snacks and amount of money the user has
# Output: first_balance 	the initial amount of money on card
def makeSelection(itemList, money):
	codeList = []
	count = 0
	itemChoice = input("Please enter one of the choices from the vending machine: ")
	
	#Creates a list of all codes
	while(count < len(itemList[0])):
		codeList.append(itemList[0][count][SNACK_CODE])
		count+=1
	
	#Checks for valid code
	while(itemChoice not in codeList):
		print("That is not a valid choice, please try again.")
		itemChoice = input("Please enter one of the choices from the vending machine: ")
	
	#Gets the index of the snack which the code is associated with
	index = 0
	while(index < len(codeList)):
		if codeList[index] == itemChoice:
			snackIndex = index
			index+=1
		else:
			index +=1
	
	#Gets the cost and quantity of choosen snack
	snackCost = float(itemList[0][snackIndex][SNACK_PRICE])		
	snackQuantity = int(itemList[0][snackIndex][SNACK_QUANTITY])
	
	#Checks if selected snack has not ran out or if user is short on money
	if(snackQuantity == 0):
		print("That is not a valid choice, please try again.")
	elif(money < snackCost):
		print("Sorry, you don't have enough money for that.")
	else:
		#if snack exists, money and quantity are subtracted
		money = money - snackCost
		snackQuantity -= 1
	
		print("Congrats, you bought a",itemList[0][snackIndex][SNACK_NAME])
		print("You now have $",money,"left on your card.")
	
	#updates quantity in list
	itemList[0][snackIndex][SNACK_QUANTITY] = snackQuantity
	
	return itemList, money 
			
# saveFile() saves current vending machine to text file 
# Input: finalList the 3d list that contains all the items
# Output:  none (new text file gets written to)
def saveFile(finalList):
	myFile = open("test.txt","w")
	count = 0
	count2 = 0
	count3 = 0
	count4 = 0
	while(count<len(finalList[0])):
		myFile.write(finalList[0][count][SNACK_NAME])
		count+=1
	while(count<len(finalList[0])):
		myFile.write(finalList[0][count2][SNACK_PRICE])
		count2+=1
	while(count<len(finalList[0])):
		myFile.write(finalList[0][count3][SNACK_QUANTITY])
		count3+=1
	while(count<len(finalList[0])):
		myFile.write(finalList[0][count4][SNACK_CODE])
		count4+=1
	myFile.close()
	
	

def main():
	# print the greeting to the user
	printGreeting()

	# read a file and create a list
	machineList = loadFile()

	# get the initial amount of money on card
	cardMoney = firstBalance()

	# ask the user the select an option
	menuChoice(machineList,cardMoney)

main()
