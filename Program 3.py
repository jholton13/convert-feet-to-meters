#input
copies = int(input('How many copies are you buying? '))

#output
if copies >= 1 and copies <= 10:
    price = 99
elif copies >= 11 and copies <= 50:
    price = 89
elif copies >= 51 and copies <= 100:
    price = 79
elif copies >= 101:
    price = 69

total = price * copies
print('The unit price is $', price)
print('The total price is $', total)
