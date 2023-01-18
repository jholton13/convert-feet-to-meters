#
# Jasmine Holton
# January 16 2023
# Write a program that calculates the cost for the total purchases:
# Ask the user to enter the number of workbooks, textbooks, and magazines being purchased.
# Calculate the total before tax.
# Calculate the amount of sales tax on the total.
# Calculate the total after tax.
# Output the total before tax, the sales tax, and the total after tax.
#

# Inputs
workbook = float(input('Enter the number of workbooks:'))
textbook = float(input('Enter the number of textbooks:'))
magazine = float(input('Enter the number of magazines:'))

# Calculations before tax
beforetax = (workbook*8.50) + (textbook*24.00) + (magazine*5.95)

# Calculations for sales tax
salestax = beforetax*.06

# Calculations for total after tax
total = beforetax+salestax

# Output
print(f'Cost before tax ${beforetax:.2f}')
print(f'Sales tax ${salestax:.2f}')
print(f'Cost after tax ${total:.2f}')
