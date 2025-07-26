Personal Finance & Savings Goal Reporter

Description
  - This is a command-line Python application designed to help users analyze their personal finances. The program takes a user's income, expenses, and a savings goal, then calculates their net monthly income and predicts whether they can achieve their savings goal within a specified timeframe. The final analysis is compiled into a clean Financial-Report.txt file.

  - The project is built using Object-Oriented Programming (OOP) principles, with logic separated into distinct modules for clarity and maintainability.
  Features
  - Dynamic Income Calculation: Converts weekly, bi-weekly, and annual income into a standard monthly figure.
  
  - Expense Tracking: Gathers multiple user expenses to calculate total monthly deductions.
  
  - Savings Goal Prediction: Determines if a user's savings goal is achievable based on their net income and desired timeframe.
  
  - Robust Error Handling: Ensures the application doesn't crash by validating user inputs for correct data types.
  
  - Modular Architecture: Code is logically separated into modules for calculations, data handling, and reporting.
  
  - File Output: Generates a persistent .txt report summarizing the user's financial situation.
  
  How to Run
  - Ensure you have Python installed on your system.
  
  - Place all four Python modules (main.py, financeCalculations.py, monthlyPay.py, displayFinanceReport.py) in the same directory.
  
  - Open a terminal or command prompt and navigate to that directory.
  
  - Run the main script using the following command: python main.py
  
  - Follow the on-screen prompts to enter your financial details.
  
  - Once completed, a Financial-Report.txt file will be created in the same directory.
  Modules
  - The application is broken down into the following modules:

1. main.py
  - Purpose: The main entry point of the application.
  - Responsibilities:
  - Handles all user interaction (gathering input for name, income, expenses, and savings goals).
  - Instantiates objects from the other modules.
  - Orchestrates the flow of data between the calculation and reporting objects.

2. financeCalculations.py
  - Purpose: A parent class that holds core financial attributes and prediction logic.
  - Class: financeCalc
  - Attributes: fullName, monthlyPay, savingsGoal, savingsGoalTimeFrame.
  - Methods:
    - predictSavingsGoal(): Calculates if the total net income over the timeframe meets the savings goal.

3. monthlyPay.py
  - Purpose: A sub-class responsible for detailed income calculations.
  - Class: calcMonthlyPay(financeCalc)
  - Responsibilities: Inherits from financeCalc.
  - Methods:
    - calcMonthIncome(): Normalizes income from various pay periods (weekly, etc.) to a monthly amount.
    - reduceIncome(): Subtracts total expenses from the monthly income to find the net amount.

4. displayFinanceReport.py
  - Purpose: Handles the creation of the final output file.
  - Class: displayReport
  - Methods:
    - outputReport(): Opens a new file named Financial-Report.txt, formats the user's financial data, and writes it to the file.

Output Example
  - After running the program, a Financial-Report.txt file will be generated with content similar to this:

|---|Financial Report|---|

Name: Alex

monthly income: $2500.0

Savings goal: reach $5000 within 6 months

Total Expenses: $1500

You are able to reach your savings goal by the time

Advice: Keep or improve your income consistency
