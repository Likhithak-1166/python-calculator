print("---SIMPLE CALCULATOR--")
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
operation=input("choose operation(+,-,*,/,%,**):")
while(operation not in ['+','-','*','/','%','**']):
    print("invalid operation")
    operation=input("choose operation(+,-,*,/,%,**):")
if operation=='+':
    result=num1+num2
elif operation=='-':
    result=num1-num2
elif operation=='*':
    result=num1*num2
elif operation=='/':
    if num2!=0:
        result=num1/num2
    else:
        result="cannot divide by zero"
elif operation=='%':
    if num2!=0:
        result=num1%num2
    else:
        result="cannot divide by zero"
elif operation=='**':
    result=num1**num2
else:
    result="invalid operation"
print("result:",result)
        