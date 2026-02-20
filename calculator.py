def add(n1, n2):
    return n1 + n2

def substraction(n1,n2):
    return n1-n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2
def calculator():
    should_accumulate=True
    num1=(input("Type the first number:"))
    while should_accumulate:
       operator=input("Type a mathematical operator (+, -, *, /): ")
       num2=(input("Type the second number:"))
       operations={"+":add,"-":substraction,"*":multiply,"/":divide}
       result=operations[operator](int(num1),int(num2))
       print(f"{num1} {operator} {num2} is {result}")
       choice=input(f"type 'y' for continue the operations with {result}")
       if choice=="y":
          num1 = result
       else:
         should_accumulate = False
         print("\n"*20)
         calculator()
calculator()