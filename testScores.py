#!/usr/bin/bash

grades = [0,0,0]	#default list to fill later
total = 0.0		#running track of test percents
count = 0.0	#counts number of tests input
for grade in grades:
	valid = False	#for validation
	while not valid:
		choice = input("Enter score in the form \"score/max\":")
		if "/" in choice:	#Test format, TODO: Update with regex?
			grade = choice.split("/")
			if grade[0].isdigit() and grade[1].isdigit():
				valid = True
				grade[0] = int(grade[0])
				grade[1] = int(grade[1])	#TODO: Check div by 0
				total += float(grade[0])/grade[1]
				count += 1
				break		#breaks loop if all validation passes
		print("An error has occurred, please check your formatting")	#validation did not pass
average = total/count*100.0
print(f"Average test grade = {average:.2f}")
if average > 95:
	print("Great work! Your average was over 95%!!!!")
