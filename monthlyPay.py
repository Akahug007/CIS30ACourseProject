# Imports  the parent class
from financeCalculations import financeCalc

# Creates a subclass of the financeCalc class
class calcMonthlyPay(financeCalc):
    # Constructor for financeCalc class
    def  __init__(self, name, income, typePay, savingsGoal, theTime):
        # Instance variables get assigned values from the parameters
        # Raises an error if the name does not contain only letters or typePay contains invalid characters
        if (not name.replace(" ", "").isalpha()):
            raise ValueError("Name must contain only letters and must be first name")
        self.fullName = name
        self.monthlyPay = income
        self.typeOfIncome = typePay
        # Calls the function calcMonthIncome to calculate the monthlyPay
        self.calcMonthIncome()
        # Calls the parent class constructor
        super().__init__(self.fullName, self.monthlyPay, savingsGoal, theTime)
    
    # Function/Method to calculate the monthly income
    def calcMonthIncome(self):
        # Conditional to check what type of payment the user has
        # If the type of income is not monthly, then the income
        # gets calculated to represent  monthly pay
        if self.typeOfIncome.isalpha():
            if self.typeOfIncome == "weekly":
                self.monthlyPay = (self.monthlyPay*52)/12
            elif self.typeOfIncome == "bi-weekly":
                self.monthlyPay = (self.monthlyPay*26)/12
            elif self.typeOfIncome == "annually":
                self.monthlyPay = self.monthlyPay/12
            else:
                self.monthlyPay = self.monthlyPay
        # Outputs the monthly income
        print("Your monthly income is: $" + str(self.monthlyPay))
    
    # Function to calculate the actual income
    def reduceIncome(self, expenses):
        # For loop to subtract the monthlyPay 
        for i in expenses:
            self.monthlyPay  -= i

        # Calls the parent class method newIncome to change the income inside the parent class
        super().newIncome(self.monthlyPay)

    # Function to get the savings prediction
    def getPrediction(self):
        return super().predictSavingsGoal()


