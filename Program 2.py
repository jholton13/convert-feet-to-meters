#Input
height = float(input('Enter the height the ball dropped from: '))
bounce = float(input('Enter the bounciness index of the ball: '))
number = int(input('Enter the number of times the ball is allowed to bounce: '))
distance = 0

#Output
for i in range(number):
    distance+=height
    height*=bounce
    distance+=height
print('The total distance traveled is:',distance,' units!')
