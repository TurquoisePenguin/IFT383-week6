#!/usr/bin/python

def main():
	initTuition = 10000	#given
	tuition = initTuition	#given
	years = 0
	while tuition < (initTuition*2):
		tuition = tuition * 1.07
		years += 1
	print(f"Tuition will be doubled in {years} years")
	print(f"Tuition will be ${tuition:.2f} in {years} years")

if __name__ == "__main__":
        main()
