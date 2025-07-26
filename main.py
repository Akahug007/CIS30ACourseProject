# Imports custom modules for calculations and reporting
from financeCalculations import financeCalc
from monthlyPay import calcMonthlyPay
from displayFinanceReport import displayReport

# Gets user's first name with exception handling
try:
    userName = str(input("What is your first name? "))
except Exception:
    print("Invalid input. Please enter your name.")
    userName = ""

# Gets user's income, ensures it's numeric
try:
    userIncome = int(input("What is your income? "))
except ValueError:
    print("Invalid input. Please enter a numeric value for income.")
    userIncome = 0

# Gets user's pay period type (weekly, bi-weekly, etc.)
try:
    userTypePay = str(input("What periodic income is it? (weekly, bi-weekly, monthly, or annually) "))
except Exception:
    print("Invalid input. Please enter the type of pay.")
    userTypePay = ""

# Gets user's savings goal, ensures it's numeric
try:
    userSavingsGoal = int(input("What is your savings goal? "))
except ValueError:
    print("Invalid input. Please enter a numeric value for savings goal.")
    userSavingsGoal = 0

# Gets duration to reach savings goal, ensures it's numeric
try:
    userSavingsTime = int(input("What's your duration to reach your goal by? (in months) "))
except ValueError:
    print("Invalid input. Please enter a numeric value for duration.")
    userSavingsTime = 0

# Gets number of expense types, ensures it's numeric
try:
    userTypeExpenses = int(input("How many types of monthly expenses do you have? "))
except ValueError:
    print("Invalid input. Please enter a numeric value for number of expenses.")
    userTypeExpenses = 0

# Collects each expense amount from the user
expensesData = []
for i in range(0, userTypeExpenses):
    try:
        expense = int(input("Whats #" + str((i+1)) + "'s expense($)? "))
        expensesData.append(expense)
    except ValueError:
        print("Invalid input. Please enter a numeric value for expense.")
        expensesData.append(0)

# Creates an object to calculate monthly pay based on user input
userMonthPayObj = calcMonthlyPay(userName, userIncome, userTypePay, userSavingsGoal, userSavingsTime)

# Calls a method to reduce the user's income by total expenses
userMonthPayObj.reduceIncome(expensesData)

# Declares a list for financial data
financialData = []

# Appends the variables to the financial data 
financialData.append(userMonthPayObj.fullName) #0
financialData.append(userMonthPayObj.monthlyPay) #1
financialData.append(userMonthPayObj.typeOfIncome) #2
financialData.append(userMonthPayObj.savingsGoal) #3
financialData.append(userMonthPayObj.savingsGoalTimeFrame) #4
financialData.append(sum(expensesData)) #5
financialData.append(userMonthPayObj.getPrediction()) #6

# Debug output the financialData list
print(financialData)

# Creates an object to create the financial report
financeReport = displayReport(financialData)

#
financeReport.outputReport()
