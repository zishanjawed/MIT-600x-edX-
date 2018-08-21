"""
Program : find the greatest sub-string of a sting (all in lower case ) entered by user

date : 07 / 29 / 2018 (mm / dd / yyyy)

@author : Zishan jawed

"""

# getting input from the user
string =  input ("Enter your sting : ") 

# In case there is any capital letter 
string = string.lower()

temp1=''
temp2=''
flag = 0    

# Traversing the string using for loop
for i in range(len(string)-1):
	if i == len(string)-1:
		if flag == 0:
			temp1 += string[i]
			break
		else:
			tepm2 = string[i]
			break

	else:
		if string[i+1] >= string[i]:
			if flag == 0:
				temp1 += string[i]
			else:
				temp2 += string[i]
		else:
			if flag == 0:
				temp1 += string[i]
			elif flag == 1:
				temp2 += string[i]
			if len(temp1) > len(temp2):
				temp2 = ''
				flag = 1
			else:
				temp1 = ''
				flag = 0

# camparing the final two sub-string
if len(temp1) > len(temp2) or len(temp1) == len(temp2):
	print("Longest substring in alphabetical order is: {}".format(temp1))
else:
	print("Longest substring in alphabetical order is: {}".format(temp2))
