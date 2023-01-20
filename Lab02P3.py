#
# Jasmine Holton
# January 18 2023
#
# Calculate discount amount for customers

# Purchase amount input
purchase = float(input('Enter  the total purchase amount: $'))

# Verify loyalty program
loyalty = input('Are you in our loyalty program? Enter "Y" for yes or "N" for no.')
x = loyalty.upper()

# Calculations for discount
five = purchase - (purchase * .05)
fifteen = purchase - (purchase * .15)
twentyFive = purchase - (purchase * .25)

# Calculations for tax
tax1 = five * .06
tax2 = fifteen * .06
tax3 = twentyFive * .06

# Calculations for total
totalFive = five + tax1
totalFifteen = fifteen + tax2
totalTwenty = twentyFive + tax3

# When customer is in the loyalty program and purchase amount is 100 or less
if x == "Y" and purchase <= 100.0:
    print(f'Your total after the discount is {fifteen:.2f}')
    print(f'Sales tax: ${tax2:.2f}')
    print(f'Total after tax: ${totalFifteen:.2f}')

    # When customer is in the loyalty program and the purchase is over 100.. 25% discount
else:
    print(f'Your total after the discount is {twentyFive:.2f}')
    print(f'Sales tax: ${tax3:.2f}')
    print(f'Total after tax: ${totalTwenty:.2f}')

# When customer is not in the loyalty program.. no discount
if x == "N" and purchase > 100:
    print(f'Your total after the discount is {five:.2f}')
    print(f'Sales tax: ${tax1:.2f}')
    print(f'Total after tax: ${totalFive:.2f}')
else:
    print('You do not qualify for a discount.')
