"""
Program : Problem 1 - Paying Debt off in a Year (MIT 600x -Pset 2)

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

@author : Zishan Jawed
"""

# taking the required information for this progarm

balance = float(input("Enter your credit card balance at month 0 : "))

annualInterestRate = float(input("Enter the annual interest rate of your credit card : "))

monthlyPaymentRate = float(input("Enter the monthly payment rate of your creddit card : "))

minimumPayment = 0

monthlyUnpaidBalance = 0

mouthlyInterestRate = 0

interest = 0

for i in range(12):
	mouthlyInterestRate = annualInterestRate /12.0
	minimumPayment = balance * monthlyPaymentRate
	monthlyUnpaidBalance = balance - minimumPayment
	balance  = monthlyUnpaidBalance + (mouthlyInterestRate*monthlyUnpaidBalance)
	
print("Remaining balance: " + str(round(balance,2)))