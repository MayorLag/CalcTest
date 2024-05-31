import math
import sys

#These functions define operations
def add(input1, input2):
    output=input1+input2
    print(str(input1)+ ' + ' + str(input2)+' = ' + str(output))
    return output

def subtract(input1, input2):
    output=input1-input2
    print(str(input1)+ ' - ' + str(input2)+' = ' + str(output))
    return output

def multiply(input1, input2):
    output=input1*input2
    print(str(input1)+ ' * ' + str(input2)+' = ' + str(output))
    return output

def divide(input1, input2):
    output=input1/input2
    print(str(input1)+ ' / ' + str(input2)+' = ' + str(output))
    return output

def power(input1, input2):
    output=input1**input2
    print(str(input1)+ ' to the power of ' + str(input2)+' = ' + str(output))
    return output

def root(input1, input2):
    root=1.0/input2
    output=input1**root
    if input2==2:
        print('Square root of ' + str(input1)+' is ' + str(output))
    else:
        print('Root ' + str(input2)+ ' of ' + str(input1)+' = ' + str(output))
    return output

#User is asked for desired operation
print('Select the operation number: \n'
      '1. Add \n'
      '2. Subtract \n'
      '3. Multiply \n'
      '4. Divide \n'
      '5. Power \n'
      '6. Root \n')

#User's choice is saved
selection=int(input('Select operation: '))

#Operation is displayed
if selection==1:
    print('x + y')

elif selection==2:
    print('x - y')

elif selection==3:
    print('x * y')

elif selection==4:
    print('x / y')

elif selection==5:
    print('x to the power of y')

elif selection==6:
    print('x to the root of y')

#X and Y numbers are requested from user
input1=float(input('Enter x: '))
input2=float(input('Enter y: '))

#Appropriate function is called and executed
if selection==1:
    add(input1,input2)

elif selection==2:
    subtract(input1,input2)

elif selection==3:
    multiply(input1,input2)

elif selection==4:
    divide(input1,input2)

elif selection==5:
    power(input1,input2)

elif selection==6:
    root(input1,input2)