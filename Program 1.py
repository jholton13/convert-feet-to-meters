#inputs
hourly = float(input('Enter your hourly wage: $ '))
regular = int(input('Enter the regular hours: '))
overtime = int(input('Enter the overtime hours: '))

#Output
print('The total weekly pay is $' + str(hourly*regular + hourly*1.5*overtime))
