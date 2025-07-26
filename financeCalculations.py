# Creates  a parent class called  financeCalc
# Subclass will calculate the salary
class financeCalc:
    # Constructor for financeCalc class
    def  __init__(self, name, monthlyIncome, goal, theTime):
        self.fullName = name
        self.monthlyPay = monthlyIncome
        self.savingsGoal = goal
        self.savingsGoalTimeFrame = theTime
    
    # Function to change the monthlyPay
    def newIncome(self, income):
        self.monthlyPay = income
    
    # Function to calculate the savingsGoal and see whether or not
    # the expenses and income would be able to reach the goal
    def predictSavingsGoal(self):
        totalPayout = (self.monthlyPay * self.savingsGoalTimeFrame)
        self.totalPayout = totalPayout
        if totalPayout >= self.savingsGoal:
            return True
        else:
            return False

