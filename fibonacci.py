n = int(input('Enter n value '))
n1 = 0
n2 = 1
count = 0
if n<=0:
    print('Invalid, please enter valid number')
elif n==1:
    print('Fibonacci series of 1 is 0')
else:
    while count<n:
        print(n1)
        nextElement = n1+n2
        n1 = n2
        n2 = nextElement
        count = count + 1