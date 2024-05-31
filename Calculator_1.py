import math
#test im losing my mind still

#These functions define operations
def add(input1, input2):
    output=input1+input2
    print(output)
    return output

def subtract(input1, input2):
    output=input1-input2
    print(output)
    return output

def multiply(input1, input2):
    output=input1*input2
    print(output)
    return output

def divide(input1, input2):
    output=input1/input2
    print(output)
    return output

def power(input1, input2):
    output=input1**input2
    print(output)
    return output

def root(input1, input2):
    root=1.0/input2
    output=input1**root
    print(output)
    return output


#User is asked for desired operation
print('Select the operation number: \n'
      '1. Add \n'
      '2. Subtract \n'
      '3. Multiply \n'
      '4. Divide \n'
      '5. Power \n'
      '6. Root \n')

#User's choice is saved, together with two numbers
selection=int(input('Select operation: '))

input1=float(input('Enter first number: '))
input2=float(input('Enter second number: '))

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

#test