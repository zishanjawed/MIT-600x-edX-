""" Problem 2
 Assume s is a string of lower case characters.
 Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your
 program should print
 Number of times bob occurs is: 2
"""
s = input("Enter your string : ")
count = 0
for i in range(len(s) - 2):
	if s[i]== 'b' and s[i+1] == 'o' and s[i+2] == 'b':
		count += 1

print("Number of times bob occurs is: ",count)