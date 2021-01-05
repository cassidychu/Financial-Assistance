def main():
    print("Welcome to our financial assistance program.\nIn order for us to assist you, we'll need some information.\nYour eligibility and amount of assistance will depend on a couple of factors.")
    moola = get_income()
    human = get_number()
    print("You entered ", moola, "for your income.")
    print("The number of children you entered was ", human)
    perChild = compute_assistance(moola, human)
    if perChild == None:
        print("You don't qualify!")
    else:
        print("Based on this information provided, you qualify for $",perChild*human, " in financial assistance!", sep ='')
        print("You are eligible to receive $", perChild, " per child based on your income.", sep ='')
  
def get_income(): 
    fin = False
    while(not fin):
        money=float(input('Please enter annual household income:'))
        if money <0:
            print("Sorry invalid income! Please try again!")
        else:
            fin=True
    return money

def get_number():
    fin=False
    while(not fin):
        menace= int(input('Please enter number of children:'))
        if menace <0:
            print("Sorry there aren't negative number of children. Enter a new number.")
        else:
            fin=True
    return menace

def compute_assistance(income, number):
    if income >=30000 and income <=40000:
        if number >=3:
            return 1000
    elif income >=20000 and income <=30000:
        if number >=2:
            return 1500
    elif income <20000:
        return 2000
    else:
        return None
        
main()
'''
#sample1
Welcome to our financial assistance program.
In order for us to assist you, we'll need some information.
Your eligibility and amount of assistance will depend on a couple of factors.

Please enter annual household income:7000

Please enter number of children:3
You entered  7000.0 for your income.
The number of children you entered was  3
Based on this information provided, you qualify for $6000 in financial assistance!
You are eligible to receive $2000 per child based on your income.       

#sample2
Welcome to our financial assistance program.
In order for us to assist you, we'll need some information.
Your eligibility and amount of assistance will depend on a couple of factors.

Please enter annual household income:6900

Please enter number of children:2
You entered  6900.0 for your income.
The number of children you entered was  2
Based on this information provided, you qualify for $4000 in financial assistance!
You are eligible to receive $2000 per child based on your income.

#sample3
Welcome to our financial assistance program.
In order for us to assist you, we'll need some information.
Your eligibility and amount of assistance will depend on a couple of factors.

Please enter annual household income:3400

Please enter number of children:1
You entered  3400.0 for your income.
The number of children you entered was  1
Based on this information provided, you qualify for $2000 in financial assistance!
You are eligible to receive $2000 per child based on your income.