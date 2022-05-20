#!usr/bin/python

def choiceFloat(inputString):
	valid = False
	while not valid:
		choice = input(inputString)
		if choice.replace(".","",1).lstrip('-').isdigit():	#removes 1 decimal point and negative, in case of float
			return float(choice)

#You could just do the math for this
def main():
	deposit = choiceFloat("Please enter the starting balance: ")
	years = 0
#	print(deposit)
	while deposit < 1000000:
		deposit = deposit*1.04
		years += 1
	print(f"In {years} years at 4% compounded interest, you will be a millionaire!!")

if __name__ == "__main__":
	main()
