import sys
print("enter the first number")
x=int(sys.stdin.readline())
print("enter the second number")
y=int(sys.stdin.readline())
def simpleadd(num1, num2):
    num1=x
    num2=y
    print("the sum is ", num1+num2)

simpleadd(x,y)
