#no of digits in a string
name = input('Enter name')
numbers = ['0','1','2','3','4','5','6','7','8','9']
count=0
for i in name:
    if i in numbers:
        count = count + 1
print(count)