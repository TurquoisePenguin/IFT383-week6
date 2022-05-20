#!/usr/bin/python

#returns a string reversed
def reverseString(string):
	output = ""
	for char in string:
		output = char + output
	return output

#returns True if palindrome, otherwise False
def isPalindrome(string):
	if string == reverseString(string):
		return True
	else:
		return False

def main():
	string = input("Enter a string: ")
	if isPalindrome(string):
		print(f"{string} is a palindrome")
	else:
		print(f"{string} is not a palindrome")

if __name__ == "__main__":
        main()


