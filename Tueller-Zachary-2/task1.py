# Zachary Tueller
# CS1400 - MO1
# Assignment 2

if __name__ == "__main__":
    investmentAmount = int(input("What is your initial investment?\n: "))
    monthlyPayment = int(input("How much are you adding each month?\n: "))
    annualInterest = int(input("What is your interest rate?\n: ")) / 100
    numYears = int(input("How long will this investment be growing?\n: "))
    monthlyInterest = (annualInterest / 12)
    time = numYears * 12
    calc1 = (1 + monthlyInterest)
    calc2 = (calc1 ** time)
    futureValue = (investmentAmount * calc2) + (monthlyPayment * ((calc2 - 1) / monthlyInterest) * calc1)
    print("Your future value is $" + str(futureValue))