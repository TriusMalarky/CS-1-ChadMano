# Zachary Tueller  
# CS1400 - MO1
# Assignment 4

if __name__ == "__main__":
    employeeName = input("What is the employee's name?\n: ")
    hours = int(input("How many hours do they work weekly?\n: "))
    rate = float(input("How much do you pay them per hour?\n: "))
    fedTax = float(input("What's the federal tax withholding rate?\n: "))
    stateTax = float(input("What's the state tax withholding rate?\n: "))
    banner = employeeName.upper() + " PAY INFORMATION"
    print(banner)
    print()
    print("\t\t\t\tPay")
    hoursString = "Hours Worked:  ".rjust(35) + str(hours).rjust(5)
    rateString = "Pay Rate: $".rjust(35) + str(rate).rjust(5)
    gross = hours * rate
    grossString = "Gross Pay: $".rjust(35) + str(gross).rjust(5)
    print(hoursString)
    print(rateString)
    print(grossString)
    print("\t\t\t\tDeductions")
    fedString = ("Federal Withholding (" + str(fedTax * 100)+"%): $").rjust(35) + str(gross * fedTax).rjust(5)
    stateString = ("State Withholding (" + str(stateTax * 100)+"%): $").rjust(35) + str(gross * stateTax).rjust(5)
    totalDed = ("Total Deduction: $").rjust(35) + str((gross * fedTax) + (gross * fedTax)).rjust(5)
    net = ("Net Pay: $").rjust(35) + str(gross - (gross * fedTax) + (gross * fedTax)).rjust(5)
    print(fedString)
    print(stateString)
    print(totalDed)
    print()
    print(net)