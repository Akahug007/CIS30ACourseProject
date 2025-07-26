class displayReport:
    # Constructor for display report class
    def __init__(self, data):
        # Financial report gets data
        self.financeReport = data

    # Main method to create a text file and
    # show the financial report
    # 6 items
    def outputReport(self):
        fout = open("Financial-Report.txt", "w")
        fout.write("\n|---|Financial Report|---|\n")
        fout.write("\n"+ "Name: " + str(self.financeReport[0]) +"\n")
        fout.write("\n"+ str(self.financeReport[2])  + " income: $" + str(self.financeReport[1]) +"\n")
        fout.write("\n"+ "Savings goal: reach $" + str(self.financeReport[3]) + " within " 
                    + str(self.financeReport[4]) + " months" +"\n")
        fout.write("\n"+ "Total Expenses: $" + str(self.financeReport[5]) +"\n")
        if self.financeReport[6]:
            fout.write("\n"+ "You are able to reach your savings goal by the time" +"\n")
            fout.write("\n"+ "Advice: Keep or improve your income consistency" +"\n")
        else:
            fout.write("\n"+ "You are not able to reach your savings goal by the time" +"\n")
            fout.write("\n"+ "Advice: Improve your income consistency" +"\n")












