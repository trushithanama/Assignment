# take 10 integers from keybord using loop and avg value
num = int(input("how many numbers: "))
total_sum = 0

for n in range (num):
    numbers = float(input('enter number:'))
    total_sum += numbers
    
avg = total_sum/num
print('average of', num,'number is :', avg)





output
how many numbers: 5
enter number:5
enter number:6
enter number:4
enter number:3
enter number:2
average of 5 number is : 4.0
>>> 
