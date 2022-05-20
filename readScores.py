#!/usr/bin/python

def main():
	scores = {}	#dictionary containing student name: test scores
	total = 0.0	#used for average calculation
	scoresFile = open("scores.txt","r")
	while not scoresFile.closed:
		line = scoresFile.readline().rstrip()
		temp = line.split(" ")		#sorry, I'm sure there's a more efficient way for this
		if line != "":
			scores[temp[0]] = [int(x) for x in temp[1:]]	#studentName: list of test scores (as int)
		else:
			scoresFile.close()
	print(f"Total number of records: {len(scores)}")
	for name in scores:
		print(f"Final score for {name} = {sum(scores[name])/len(scores[name])}%")
		total += sum(scores[name])/len(scores[name])
	print(f"Class Average = {total/len(scores):.2f}")

if __name__ == "__main__":
        main()

