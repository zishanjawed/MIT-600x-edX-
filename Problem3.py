"""
Program : Problem 3 - Using Bisection Search to Make the Program Faster (MIT 600x)

mathematicle terms:
		Monthly interest rate = (Annual interest rate) / 12.0
		Monthly payment lower bound = Balance / 12
		Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

@author : Zishan Jawed

"""
balance = float(input("Enter your credit card balance at month 0 : "))

annualInterestRate = float(input("Enter the annual interest rate of your credit card : "))

monthlyInterastRate = annualInterestRate / 12.0

lowerBound = balance /12

upperBound = (balance * (1 + monthlyInterastRate)**12) /12.0

balanceUpdate = 0

ans = (upperBound + lowerBound) / 2

epcilon = 0.03

while abs(balanceUpdate) >= epcilon:
	balanceUpdate = balance
	ans = (upperBound + lowerBound) / 2
	for i in range(12):    
		monthlyUnpaidBalance = balanceUpdate - ans
		balanceCopy = monthlyUnpaidBalance + (mouthlyInterestRate* monthlyUnpaidBalance)
	if balanceUpdate > epcilon:
		lowerBound = ans
	elif balanceUpdate < epcilon:
		upperBound = ans
	else:
		break
	

print("Lowest Payment: {}".format(round(ans,2)))

	