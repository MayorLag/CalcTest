import math
import sys

#These functions define operations
def add(input1, input2):
    result=input1+input2
    return(str(input1)+ ' + ' + str(input2)+' = ' + str(result))

def subtract(input1, input2):
    result=input1-input2
    return(str(input1)+ ' - ' + str(input2)+' = ' + str(result))

def multiply(input1, input2):
    result=input1*input2
    return(str(input1)+ ' * ' + str(input2)+' = ' + str(result))

def divide(input1, input2):
    if input2==0:
        return ('Stop dividing by zero!')
    else:
        result=input1/input2
        return(str(input1)+ ' / ' + str(input2)+' = ' + str(result))

def power(input1, input2):
    result=input1**input2
    return(str(input1)+ ' to the power of ' + str(input2)+' = ' + str(result))
    
def root(input1, input2):
    root=1.0/input2
    result=input1**root
    if input2==2:
        return('Square root of ' + str(input1)+' is ' + str(result))
    else:
        return('Root ' + str(input2)+ ' of ' + str(input1)+' = ' + str(result)) 

#Selection number is matched to a function
dictionary={
    1: add, 
    2: subtract, 
    3: multiply, 
    4: divide, 
    5: power, 
    6: root}

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

#Operation is displayed for user clarity
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

#Function is called from dictionary
if selection in dictionary:
    function=dictionary[selection](input1,input2)
    print(str(function))
else:
    print('Invalid selection')