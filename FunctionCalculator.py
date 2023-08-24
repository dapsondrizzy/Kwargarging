def add(a,b):
    return a + b    

def subtract(a,b):
    return a - b

def divide(a,b):
    return a / b

def multiply(a,b):
    return a * b

print('select operator')
print('1.add')
print('2.subtract')
print('3.divide')
print('4.multiply')

while True:
    f=input('choose your operator:')
    if f in ('1','2','3','4'):
      try:
        n=float(input('enter your number:'))
        y=float(input('enter your second number:'))
      except ValueError:
        print ('please choose an integer value')
        continue
    
    if f=='1': 
        print(n ,'+', y ,'=',add(n,y))
    elif f=='2':
        print(n, '-', y ,'=',subtract(n,y))
    elif f =='3':
        print(n ,'/', y , '=', divide(n,y))
    elif f=='4':
        print(n, '*', y ,'=',multiply(n,y))

    another=input('wanna run another code (yes/no)?:')
    if another == 'no': 
        break
else:
    print('Running')
    

