#!/usr/bin/python
def firstName(name):
	return name.split(" ")[0]

def main():
	name = input("Please enter your full name: ")
	print(f"Hello {firstName(name)}")

if __name__ == "__main__":
        main()

