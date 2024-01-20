def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "cannot divide by zero"
    
def calculator():
    while True:
        print("Select operration:")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")

        choice=input("Enter choice (1/2/3/4/5):")
            
        if choice in ('1','2','3','4'):
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))

            if choice == '1':
                print(num1,"+",num2,"=",add(num1,num2))
            if choice == '2':
                print(num1,"-",num2,"=",subtract(num1,num2))
            if choice == '3':
                print(num1,"*",num2,"=",multiply(num1,num2))
            if choice == '4':
                result=divide(num1,num2)
                print(num1,"/",num2,"=",result)
            else:
                print("Invalid Input")

        elif choice == '5':
            print("Exiting the calculator")
            break
        else:
            print("Invalid Input.Provide a valid input")

calculator()


