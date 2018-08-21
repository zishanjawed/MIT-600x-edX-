"""
Program : Calculate the minimum monthly fixed payment (MIT 600x -Pset 2)

more detail :
	 write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

Mathematical terms:
   					Monthly interest rate = (Annual interest rate) / 12.0
					Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
					Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 

@author : ZIHSAN JAWED
"""
balance = float(input("Enter your credit card balance at month 0 : "))

annualInterestRate = float(input("Enter the annual interest rate of your credit card : "))

minimumPayment = 0

monthlyUnpaidBalance = 0

mouthlyInterestRate = annualInterestRate/12.0

minimumFixedMonthlyPayment = 0

balanceCopy = balance

while balanceCopy > 0:
	balanceCopy = balance
	minimumFixedMonthlyPayment += 10
	for i in range(12):
		monthlyUnpaidBalance = balanceCopy - minimumFixedMonthlyPayment
		balanceCopy = monthlyUnpaidBalance + (mouthlyInterestRate* monthlyUnpaidBalance)

print("Lowest Payment: " + str(minimumFixedMonthlyPayment))