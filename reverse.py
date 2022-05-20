#!/usr/bin/python

def main():
	inputString = input("Please enter a word: ")
	outputString = ""
	for char in inputString:
		outputString = char + outputString
	print(f"The reverse of {inputString} is {outputString}")

if __name__ == "__main__":
	main()
